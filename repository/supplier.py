from sqlalchemy.orm import Session

from models.supplier import Supplier

def create(db: Session, supplier: Supplier) -> Supplier:
    db.add(supplier)
    db.flush()
    return supplier

def get_supplier_by_id(
    db: Session,
    product_supplier_id: int
) -> Supplier | None:
    return (
        db.query(Supplier)
        .filter(Supplier.id == product_supplier_id)
        .first()
    )

def get_product_suppliers(
    db: Session
) -> list[Supplier]:
    return db.query(Supplier).all()

def get_some_suppliers(
    db: Session,
    supplier_ids: list[int]
) -> list[Supplier]:
    return db.query(Supplier).filter(Supplier.id.in_(supplier_ids)).all()

def delete_product_supplier(
    db: Session,
    supplier: Supplier,
) -> None:
    db.delete(supplier)
    db.flush()
