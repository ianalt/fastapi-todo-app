from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from starlette import status

from TodoApp.database import SessionLocal
from TodoApp.models import Todo, User
from routers.auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


class GetUserInfoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str
    email: str
    first_name: str
    last_name: str
    role: str


class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str

@router.get("/current", response_model=GetUserInfoResponse)
async def get_user_info(db: db_dependency, current_user: user_dependency):
    if current_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    user = db.query(User).filter(User.id == current_user.get("id")).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    response = GetUserInfoResponse.model_validate(user)

    return response


@router.patch("/change-password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(db: db_dependency, current_user: user_dependency, body_req:  ChangePasswordRequest):
    if current_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    user = db.query(User).filter(User.id == current_user.get("id")).first()

    password_matches = bcrypt_context.verify(body_req.current_password, user.hashed_password)

    if not password_matches:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect password")

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    user.hashed_password = bcrypt_context.hash(body_req.new_password)

    db.add(user)
    db.commit()