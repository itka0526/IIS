from sqlalchemy.orm import Session
from app.db.models import Issue, Book, Reader
from app.models.issue import IssueCreate


class IssueService:
    @staticmethod
    def create_issue(db: Session, issue_data: IssueCreate):
        book = db.query(Book).filter(Book.id == issue_data.book_id).first()
        if not book:
            raise ValueError(f"Книга с ID {issue_data.book_id} не найдена")
        existing_issue = db.query(Issue).filter(Issue.book_id == issue_data.book_id).first()
        if existing_issue:
            raise ValueError(f"Книга с ID {issue_data.book_id} уже выдана")

        reader = db.query(Reader).filter(Reader.id == issue_data.reader_id).first()
        if not reader:
            raise ValueError(f"Читатель с ID {issue_data.reader_id} не найден")

        issue = Issue(**issue_data.dict())
        db.add(issue)
        db.commit()
        db.refresh(issue)
        return issue

    @staticmethod
    def get_issue(db: Session, issue_id: int):
        issue = db.query(Issue).filter(Issue.id == issue_id).first()
        if not issue:
            raise ValueError(f"Выдача с ID {issue_id} не найдена")
        return issue

    @staticmethod
    def get_all_issues(db: Session):
        return db.query(Issue).all()

    @staticmethod
    def close_issue(db: Session, issue_id: int):
        issue = db.query(Issue).filter(Issue.id == issue_id).first()
        if not issue:
            raise ValueError(f"Выдача с ID {issue_id} не найдена")
        db.delete(issue)
        db.commit()
        return {"message": f"Выдача с ID {issue_id} закрыта"}
