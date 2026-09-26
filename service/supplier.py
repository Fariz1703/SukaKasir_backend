from sqlalchemy.orm import Session

from models.supplier import Supplier
from schemas.supplier import SupplierCreate, SupplierUpdate

def create_supplier(
    db: Session,
    supplier_data: SupplierCreate
) -> Supplier:

    supplier = Supplier(
        name=supplier_data.name,
        description=supplier_data.description,
    )

    db.add(supplier)
    db.commit()
    db.refresh(supplier)

    return supplier

def get_supplier(
    db: Session,
    supplier_id: int
) -> Supplier | None:

    return (
        db.query(Supplier)
        .filter(Supplier.id == supplier_id)
        .first()
    )

def get_suppliers(
    db: Session
) -> list[Supplier]:

    return db.query(Supplier).all()

def update_supplier(
    db: Session,
    supplier_id: int,
    supplier_data: SupplierUpdate
) -> Supplier | None:

    supplier = get_supplier(db, supplier_id)

    if supplier is None:
        return None

    if supplier_data.name is not None:
        supplier.name = supplier_data.name

    if supplier_data.description is not None:
        supplier.description = supplier_data.description

    db.commit()

    return supplier

def delete_supplier(
    db: Session,
    supplier_id: int
) -> Supplier | None:

    supplier = get_supplier(db, supplier_id)

    if supplier is None:
        return None

    db.delete(supplier)
    db.commit()

    return supplier