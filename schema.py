# Imports
from pydantic import BaseModel


# Schema for book
class Book(BaseModel):
    title: str
    rating: int
    author_id: int

    class Config:
        orm_mode = True
        json_schema_extra = {
            "examples": [{"title": "The Great Gatsby", "rating": 10, "author_id": 1}]
        }


# Schema for author
class Author(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True
        json_schema_extra = {"examples": [{"name": "F. Scott Fitzgerald", "age": 40}]}
