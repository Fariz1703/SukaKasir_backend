from sqlalchemy import exc
from sqlalchemy.orm import Session
from fastapi import status

from core.exception import AppException
from models.category import Category
from repository import category as category_repository
from schemas.common import category
from schemas.common.category import CategoryCreate, CategoryUpdate


def create_category(
    db: Session,
    category_data: CategoryCreate,
) -> Category:

    category = Category(
        name=category_data.name,
        description=category_data.description,
    )

    try:
        category_repository.create(db, category)
        db.commit()
        db.refresh(category)
        return category

    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to create category",
        ) from exc


def get_category(
    db: Session,
    category_id: int
) -> Category | None:

    return category_repository.get_category_by_id(db, category_id)

def get_categories(
    db: Session
) -> list[Category]:

    return category_repository.get_categories(db)

def update_category(
    db: Session,
    category_id: int,
    category_data: CategoryUpdate
) -> Category | None:

    category = category_repository.get_category_by_id(db, category_id)

    if category is None:
        return None

    if category_data.name is not None:
        category.name = category_data.name

    if category_data.description is not None:
        category.description = category_data.description


    try:
        db.commit()
        db.refresh(category)
        return category

    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to update category",
        ) from exc



def delete_category(
    db: Session,
    category_id: int
) -> Category | None:

    category = category_repository.get_category_by_id(db, category_id)

    if category is None:
        return None

    try:
        category_repository.delete_category(db, category)
        db.commit()
        return category

    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to delete category",
        ) from exc