from sqlalchemy.orm import Session

from helper.commitDbHelper import commit_db
from models.category import Category
from schemas.common import category
from schemas.common.category import CategoryCreate, CategoryUpdate


def create_category(
    db: Session,
    category_data: CategoryCreate
) -> Category:

    category = Category(
        name=category_data.name,
        description=category_data.description
    )

    commit_db(db, category)

    return category


def get_category(
    db: Session,
    category_id: int
) -> Category | None:

    return (
        db.query(Category)
        .filter(Category.id == category_id)
        .first()
    )


def get_categories(
    db: Session
) -> list[Category]:

    return db.query(Category).all()


def update_category(
    db: Session,
    category_id: int,
    category_data: CategoryUpdate
) -> Category | None:

    category = get_category(db, category_id)

    if category is None:
        return None

    if category_data.name is not None:
        category.name = category_data.name

    if category_data.description is not None:
        category.description = category_data.description


    commit_db(db, category)

    return category


def delete_category(
    db: Session,
    category_id: int
) -> Category | None:

    category = get_category(db, category_id)

    if category is None:
        return None

    
    commit_db(db, category)

    return category