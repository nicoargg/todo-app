from http.client import HTTPException
from urllib import response
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from model import Todo

# App object
app = FastAPI()


from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/todo/")
async def get_todos():
    response = await fetch_all_todos()
    return response


@app.get("/api/todo/{_id}/", response_model=Todo)
async def get_todo_by_title(title):
    response = fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no ToDo item with title {title}")


@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(404, "Something went wrong")

@app.put("/api/todo/{_id}/")
async def update_todo(title:str, description:str):
    response = await update_todo(title, description)
    if response:
        return response
    raise HTTPException(404, f"There is no ToDo item with title {title}")

@app.delete("/api/todo/{_id}/")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no ToDo item with title {title}")
