from sqlalchemy.orm import DeclarativeBase ,sessionmaker
from sqlalchemy import create_engine


from core.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(
    settings.DATABASE_URL
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)