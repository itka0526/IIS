from fastapi import APIRouter, HTTPException
from app.models import Book
from app.database import get_all_books, get_book, add_book, update_book, delete_book

router = APIRouter()


@router.get("/book/all", response_model=list[Book])
async def read_books():
    """Получить список всех книг."""
    return get_all_books()


@router.get("/book/{book_id}", response_model=Book)
async def read_book(book_id: int):
    """Получить книгу по ID."""
    book = get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@router.post("/book", response_model=Book)
async def create_book(book: Book):
    """Добавить новую книгу."""
    book_data = book.model_dump()  # Convert Pydantic model to a dict
    book_id = add_book(book_data)  # Add book to database
    return get_book(book_id)  # Return the newly added book


@router.put("/book/{book_id}", response_model=Book)
async def update_book_info(book_id: int, book: Book):
    """Обновить информацию о книге."""
    existing_book = get_book(book_id)
    if existing_book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    updated_book = update_book(book_id, book.model_dump(exclude_unset=True))  # Update the book info
    return updated_book


@router.delete("/book/{book_id}")
async def delete_book_info(book_id: int):
    """Удалить книгу по ID."""
    if get_book(book_id) is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    delete_book(book_id)  # Delete the book from the database
    return {"message": "Книга успешно удалена"}
