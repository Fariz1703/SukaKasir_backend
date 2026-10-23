
from sqlalchemy.orm import Session
from fastapi import status

from models.productSupplier import ProductSupplier
from repository import productSupplier as product_supplier_repository
from core.exception import AppException
from schemas.common import category
from schemas.common.productSupplier import ProductSupplierCreate, ProductSupplierUpdate

def create_product_supplier(
    db: Session,
    product_supplier_data: ProductSupplierCreate
) -> ProductSupplier:

    product_supplier = ProductSupplier(
        product_id=product_supplier_data.product_id,
        supplier_id=product_supplier_data.supplier_id,
        buy_price=product_supplier_data.buy_price
    )

    try:
        product_supplier_repository.create(db, product_supplier)
        db.commit()
        db.refresh(product_supplier)
        return product_supplier

    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to create product supplier",
        ) from exc


def get_product_supplier(
    db: Session,
    product_supplier_id: int
) -> ProductSupplier | None:

    return product_supplier_repository.get_product_supplier_by_id(db, product_supplier_id)

def get_product_suppliers(
    db: Session
) -> list[ProductSupplier]:

    return product_supplier_repository.get_product_suppliers(db)

def update_product_supplier(
    db: Session,
    product_supplier_id: int,
    product_supplier_data: ProductSupplierUpdate
) -> ProductSupplier | None:

    product_supplier = product_supplier_repository.get_product_supplier_by_id(db, product_supplier_id)

    if not product_supplier:
        return None

    if product_supplier_data.product_id is not None:
        product_supplier.product_id = product_supplier_data.product_id
    if product_supplier_data.supplier_id is not None:
        product_supplier.supplier_id = product_supplier_data.supplier_id
    if product_supplier_data.buy_price is not None:
        product_supplier.buy_price = product_supplier_data.buy_price

    try:
        db.commit()
        db.refresh(product_supplier)
        return product_supplier

    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to update product supplier",
        ) from exc

def delete_product_supplier(
    db: Session,
    product_supplier_id: int
) -> ProductSupplier | None:

    product_supplier = get_product_supplier(db, product_supplier_id)

    if product_supplier is None:
        return None

    try:
        product_supplier_repository.delete_product_supplier(db, product_supplier)
        db.commit()
        return product_supplier
    
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to delete product supplier",
        ) from exc
