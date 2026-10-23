from sqlalchemy.orm import Session
from fastapi import status

from core.exception import AppException
from models.supplier import Supplier
from repository import productSupplier as productSupplier_repository
from schemas.common.supplier import SupplierCreate, SupplierUpdate

def create_supplier(
    db: Session,
    supplier_data: SupplierCreate
) -> Supplier:

    supplier = Supplier(
        name=supplier_data.name,
        description=supplier_data.description,
    )

    try:
        productSupplier_repository.create(db, supplier)
        db.commit()
        db.refresh(supplier)
        return supplier

    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to create supplier",
        ) from exc


def get_supplier(
    db: Session,
    supplier_id: int
) -> Supplier | None:

    return productSupplier_repository.get_product_supplier_by_id(db, supplier_id)

def get_suppliers(
    db: Session
) -> list[Supplier]:

    return productSupplier_repository.get_product_suppliers(db)

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

    try:
        db.commit()
        db.refresh(supplier)
        return supplier

    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to update supplier",
        ) from exc

def delete_supplier(
    db: Session,
    supplier_id: int
) -> Supplier | None:

    supplier = get_supplier(db, supplier_id)

    if supplier is None:
        return None

    try:
        productSupplier_repository.delete_product_supplier(db, supplier)
        db.commit()
        return supplier

    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to delete supplier",
        ) from exc
    