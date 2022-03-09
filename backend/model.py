from pydantic import BaseModel

from bson import ObjectId

from fastapi.encoders import jsonable_encoder

class Todo(BaseModel):
    title: str
    description: str

    class Config:
        json_encoders = {ObjectId: str}