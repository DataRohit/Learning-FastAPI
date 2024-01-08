# Import dataclass
from dataclasses import dataclass
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


# Initialize Base
Base = declarative_base()


# Class to represent a book
@dataclass
class Book(Base):
    # Give a name to the table
    __tablename__ = "book"

    # Add columns to the table
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    rating = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    author_id = Column(Integer, ForeignKey("author.id"))

    # Create a relationship between the book and the author
    author = relationship("Author")


# Class to represent an author
@dataclass
class Author(Base):
    # Give a name to the table
    __tablename__ = "author"

    # Add columns to the table
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
