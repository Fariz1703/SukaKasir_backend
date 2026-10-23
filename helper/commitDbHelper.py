from sqlalchemy.orm import Session
from typing import TypeVar

from fastapi import status

from core.exception import AppException

T = TypeVar("T")


def commit_db(db: Session, data:T) -> T:
    try:
        db.add(data)
        db.commit()
        db.refresh(data)

        return data

    except Exception as exc:
        db.rollback()

        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to save data to the database",
        ) from exc