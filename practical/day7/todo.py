from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from starlette import status

app = FastAPI()

class todo_create(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    completed: Optional[bool] = None

class todo(todo_create):
    id: int
    created_at: datetime

todo_list: dict[int, todo] = {}
count = 0


def get_todo_or_404(todo_id: int):
    if todo_list.get(todo_id):
        return todo_list.get(todo_id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo is not in the list")

@app.get("/todos", response_model=list[todo])
def todos(completed: Optional[bool] = None):
    todo = list(todo_list.values())
    if completed:
      todo =  [t for t in todo_list if t.completed == completed]

    return todo


@app.get("/todos/{todo_id}", response_model=todo)
def get_todo_with_id(todo_id: int, todo: todo = Depends(get_todo_or_404)):
    return todo

@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(todo: todo_create):
    global count
    count += 1
    todo_list[count] = {
        "id": count,
        "created_at": datetime.now(),
        **todo.model_dump()
    }
    return todo_list[count]


@app.put("/todos/{todo_id}", status_code=status.HTTP_202_ACCEPTED)
def update_todo(todo_id: int, todo_create: todo_create, todo: todo = Depends(get_todo_or_404)):
    todo_list[todo_id] = {
        "id": todo_id,
        "created_at": todo["created_at"],
        **todo_create.model_dump()
    }
    return todo_list[todo_id]


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, todo: todo = Depends(get_todo_or_404)):
    del todo_list[todo_id]

