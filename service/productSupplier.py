from sqlalchemy.orm import Session

from models.productSupplier import ProductSupplier
from schemas.productSupplier import ProductSupplierCreate, ProductSupplierUpdate

def create_product_supplier(
    db: Session,
    product_supplier_data: ProductSupplierCreate
) -> ProductSupplier:

    product_supplier = ProductSupplier(
        product_id=product_supplier_data.product_id,
        supplier_id=product_supplier_data.supplier_id,
        buy_price=product_supplier_data.buy_price
    )

    db.add(product_supplier)
    db.commit()
    db.refresh(product_supplier)

    return product_supplier

def get_product_supplier(
    db: Session,
    product_supplier_id: int
) -> ProductSupplier | None:

    return (
        db.query(ProductSupplier)
        .filter(ProductSupplier.id == product_supplier_id)
        .first()
    )

def get_product_suppliers(
    db: Session
) -> list[ProductSupplier]:

    return db.query(ProductSupplier).all()

def update_product_supplier(
    db: Session,
    product_supplier_id: int,
    product_supplier_data: ProductSupplierUpdate
) -> ProductSupplier | None:

    product_supplier = (
        db.query(ProductSupplier)
        .filter(ProductSupplier.id == product_supplier_id)
        .first()
    )

    if not product_supplier:
        return None

    if product_supplier_data.product_id is not None:
        product_supplier.product_id = product_supplier_data.product_id
    if product_supplier_data.supplier_id is not None:
        product_supplier.supplier_id = product_supplier_data.supplier_id
    if product_supplier_data.buy_price is not None:
        product_supplier.buy_price = product_supplier_data.buy_price

    db.commit()
    db.refresh(product_supplier)

    return product_supplier

def delete_product_supplier(
    db: Session,
    product_supplier_id: int
) -> ProductSupplier | None:

    product_supplier = get_product_supplier(db, product_supplier_id)

    if product_supplier is None:
        return None

    db.delete(product_supplier)
    db.commit()

    return product_supplier