from typing import Annotated
from fastapi import Depends, HTTPException, Path, APIRouter
from pydantic import BaseModel, Field
from starlette import status
from TodoApp.database import SessionLocal
from sqlalchemy.orm import Session
from TodoApp.models import Todo

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class TodoRequest(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


@router.get("/todos", status_code=status.HTTP_200_OK)
async def find_all_todos(db: db_dependency):
    return db.query(Todo).all()


@router.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def find_by_id(db: db_dependency, todo_id: Annotated[int, Path(gt=0)]):
    found_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if found_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return found_todo


@router.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, body_req: TodoRequest):
    try:
        new_todo = Todo(**body_req.model_dump())
        db.add(new_todo)
        db.commit()
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.put("/todos/{todo_id}", status_code=status.HTTP_201_CREATED)
async def update_todo(db: db_dependency, todo_id: Annotated[int, Path(gt=0)], body_req: TodoRequest):
    found_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if found_todo is None:
        raise HTTPException(status_code=404, detail="TODO not found")

    found_todo.title = body_req.title
    found_todo.description = body_req.description
    found_todo.priority = body_req.priority
    found_todo.complete = body_req.complete

    db.add(found_todo)
    db.commit()


@router.delete("/todos/{todo_id}", status_code=status.HTTP_201_CREATED)
async def delete_todo(db: db_dependency, todo_id: Annotated[int, Path(gt=0)], body_req: TodoRequest):
    found_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if found_todo is None:
        raise HTTPException(status_code=404, detail="TODO not found")

    db.query(Todo).filter(Todo.id == todo_id).delete()

    db.commit()
