from sqlalchemy.orm import Session

from models.product import Product
from schemas.product import ProductCreate, ProductUpdate


def create_product(
    db: Session,
    product_data: ProductCreate
) -> Product:

    product = Product(
        name=product_data.name,
        category_id=product_data.category_id,
        unit_id=product_data.unit_id,
        sku=product_data.sku,
        unit_size=product_data.unit_size,
        sell_price=product_data.sell_price,
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product

def get_product(
    db: Session,
    product_id: int
) -> Product | None:

    return (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

def get_some_product(
    db: Session,
    product_id: list[int]
) -> list[Product]:

    return (
        db.query(Product)
        .filter(Product.id.in_(product_id))
        .all()
    )


def get_products(
    db: Session
) -> list[Product]:

    return db.query(Product).all()

def update_product(
    db: Session,
    product_id: int,
    product_data: ProductUpdate
) -> Product | None:

    product = get_product(db, product_id)

    if product is None:
        return None

    if product_data.name is not None:
        product.name = product_data.name
    if product_data.category_id is not None:
        product.category_id = product_data.category_id
    if product_data.unit_id is not None:
        product.unit_id = product_data.unit_id
    if product_data.sku is not None:
        product.sku = product_data.sku
    if product_data.unit_size is not None:
        product.unit_size = product_data.unit_size
    if product_data.sell_price is not None:
        product.sell_price = product_data.sell_price

    db.commit()
    db.refresh(product)

    return product


def delete_product(
    db: Session,
    product_id: int
) -> Product | None:

    product = get_product(db, product_id)

    if product is None:
        return None

    db.delete(product)
    db.commit()

    return product