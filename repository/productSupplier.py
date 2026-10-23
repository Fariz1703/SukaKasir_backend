from sqlalchemy.orm import Session

from models.productSupplier import ProductSupplier

def create(db: Session, productSupplier: ProductSupplier) -> ProductSupplier:
    db.add(productSupplier)
    db.flush()
    return productSupplier

def get_product_supplier_by_id(
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

def get_some_product_suppliers(
    db: Session,
    product_supplier_ids: list[int]
) -> list[ProductSupplier]:
    return db.query(ProductSupplier).filter(ProductSupplier.id.in_(product_supplier_ids)).all()

def delete_product_supplier(
    db: Session,
    productSupplier: ProductSupplier,
) -> None:
    db.delete(productSupplier)
    db.flush()
