from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.book_service import BookService
from app.db.sessions import get_db
from app.models.book import BookCreate, BookResponse

router = APIRouter()


@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    try:
        return BookService.create_book(db, book)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{id}", response_model=BookResponse)
def get_book(id: int, db: Session = Depends(get_db)):
    try:
        return BookService.get_book(db, id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{id}")
def delete_book(id: int, db: Session = Depends(get_db)):
    try:
        return BookService.delete_book(db, id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def get_all_books(db: Session = Depends(get_db)):
    try:
        return BookService.get_all_books(db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
