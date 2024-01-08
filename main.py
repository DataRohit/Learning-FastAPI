# Imports
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

# Import model and schema
from models import (
    Book as ModelBook,
    Author as ModelAuthor,
)
from schema import (
    Book as SchemaBook,
    Author as SchemaAuthor,
)


# Load env variables
load_dotenv(".env")


# Initialize FastAPI
app = FastAPI()


# Set up middleware
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


# Base route
@app.get("/")
async def index():
    # Return a JSON response
    return {"message": "Hello, World!"}


# Route for adding a book to the database
@app.post("/add-book/", response_model=SchemaBook)
async def add_book(book: SchemaBook):
    # Create a book instance
    db_book = ModelBook(title=book.title, rating=book.rating, author_id=book.author_id)

    # Save the book instance to the database
    db.session.add(db_book)

    # Commit the changes
    db.session.commit()

    # Return the book instance as JSON
    return db_book


# Route for adding an author to the database
@app.post("/add-author/", response_model=SchemaAuthor)
async def add_author(author: SchemaAuthor):
    # Create an author instance
    db_author = ModelAuthor(name=author.name, age=author.age)

    # Save the author instance to the database
    db.session.add(db_author)

    # Commit the changes
    db.session.commit()

    # Return the author instance as JSON
    return db_author


# Route to list all books
@app.get("/books/")
def get_books():
    # Get all books from the database
    db_books = db.session.query(ModelBook).all()

    # Convert each book instance to a dictionary
    books_as_dict = [
        {
            "title": book.title,
            "rating": book.rating,
            "author_id": book.author_id,
            "time_created": book.time_created,
            "time_updated": book.time_updated,
        }
        for book in db_books
    ]

    # Return the books as JSON
    return books_as_dict
