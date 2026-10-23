from sqlalchemy.orm import Session

from models.category import Category

def create(db: Session, category: Category) -> Category:
    db.add(category)
    db.flush()
    return category

def get_category_by_id(
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

def delete_category(
    db: Session,
    category: Category,
) -> None:
    db.delete(category)
    db.flush()
