from sqlalchemy.orm import Session

from models.product import Product

def create(db: Session, product: Product) -> Product:
    db.add(product)
    db.flush()
    return product

def get_product_by_id(
    db: Session,
    product_id: int
) -> Product | None:
    return (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

def get_products(
    db: Session
) -> list[Product]:
    return db.query(Product).all()


def get_some_products(
    db: Session,
    product_ids: list[int]
) -> list[Product]:
    return db.query(Product).filter(Product.id.in_(product_ids)).all()

def delete_product(
    db: Session,
    product: Product,
) -> None:
    db.delete(product)
    db.flush()
