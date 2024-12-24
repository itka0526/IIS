from pydantic import BaseModel
from typing import Optional


class Book(BaseModel):
    id: Optional[int] = None  # Идентификатор книги
    title: str  # Название книги
    author: str  # Автор книги
    year: int  # Год издания книги
