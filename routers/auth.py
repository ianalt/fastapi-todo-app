from datetime import timedelta, datetime, timezone
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status

from TodoApp.database import SessionLocal
from TodoApp.models import User

SECRET_KEY = "c780be6bb34b32e2ca782266a3f8c4adfbc00a500116739b3b87265b0b582a31"
ALGORITHM = "HS256"
router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/auth")


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    phone_number: str
    password: str
    role: str


class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()

    if not user or not bcrypt_context.verify(password, user.hashed_password):
        return False

    return user


def create_access_token(username: str, user_id: int, user_role: str, expires_delta: timedelta):
    current_date = datetime.now(timezone.utc)

    encode = {
        "sub": username,
        "id": user_id,
        "role": user_role,
        "exp": int((current_date + expires_delta).timestamp())
    }

    access_token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    return access_token


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        user_role: str = payload.get("role")

        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

        return {
            "username": username,
            "id": user_id,
            "user_role": user_role
        }

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")


db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    authenticated_user = authenticate_user(form_data.username, form_data.password, db)

    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token = create_access_token(username=authenticated_user.username, user_id=authenticated_user.id, user_role=authenticated_user.role,
                                       expires_delta=timedelta(minutes=20))

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.post("/register-user", status_code=status.HTTP_201_CREATED)
async def register_user(db: db_dependency,
                        body_req: CreateUserRequest):
    created_user = User(
        email=body_req.email,
        username=body_req.username,
        first_name=body_req.first_name,
        last_name=body_req.last_name,
        role=body_req.role,
        hashed_password=bcrypt_context.hash(body_req.password),
        is_active=True,
        phone_number=body_req.phone_number,
    )

    db.add(created_user)
    db.commit()
