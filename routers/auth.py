from typing import Annotated

from fastapi import APIRouter, Depends
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status

from TodoApp.database import SessionLocal
from TodoApp.models import User

router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
                      body_req: CreateUserRequest):
    created_user = User(
        email=body_req.email,
        username=body_req.username,
        first_name=body_req.first_name,
        last_name=body_req.last_name,
        role=body_req.role,
        hashed_password=bcrypt_context.hash(body_req.password),
        is_active=True
    )

    db.add(created_user)
    db.commit()
