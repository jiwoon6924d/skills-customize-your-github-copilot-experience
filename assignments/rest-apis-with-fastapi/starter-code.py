from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")

items = [
    {"id": 1, "name": "Write code", "done": False},
    {"id": 2, "name": "Review notes", "done": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI task API!"}


# TODO: Add a Pydantic model for new items
# TODO: Create GET /items and GET /items/{item_id}
# TODO: Add POST /items, PUT /items/{item_id}, and DELETE /items/{item_id}
