from app.db.models import Base
from app.db.sessions import engine


def init_db():
    Base.metadata.create_all(bind=engine)
