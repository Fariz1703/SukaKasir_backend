from fastapi import APIRouter, Depends, HTTPException, status
from core.exception import AppException
from sqlalchemy.orm import Session

from core.exception import AppException
from database.dependency import get_db
from schemas.respons import ResponseSchema
from schemas.supplier import (
    SupplierCreate,
    SupplierResponse,
    SupplierUpdate,
)
from service.supplier import (
    create_supplier,
    get_suppliers,
    get_supplier,
    update_supplier,
    delete_supplier,
)

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)

@router.post(
    "",
    response_model=ResponseSchema[SupplierResponse],
    status_code=status.HTTP_201_CREATED
)
def create(
    supplier_data: SupplierCreate,
    db: Session = Depends(get_db)
):
    supplier = create_supplier(db, supplier_data)

    if supplier is None:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Failed to create Supplier"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_201_CREATED,
        "message" : "Supplier created succesfully",
        "data" : supplier
    }

@router.get(
    "",
    response_model=ResponseSchema[list[SupplierResponse]]
)
def get_all(
    db: Session = Depends(get_db)
):
    suppliers = get_suppliers(db)

    if suppliers is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Suppliers not found"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Suppliers retrieved succesfully",
        "data" : suppliers
    }


@router.get(
    "/{supplier_id}",
    response_model=ResponseSchema[SupplierResponse]
)
def get_one(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    supplier = get_supplier(db, supplier_id)

    if supplier is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Supplier not found"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Supplier retrieved succesfully",
        "data" : supplier
    }

@router.patch(
    "/{supplier_id}",
    response_model=ResponseSchema[SupplierResponse]
)
def update(
    supplier_id: int,
    supplier_data: SupplierUpdate,
    db: Session = Depends(get_db)
):
    supplier = update_supplier(db, supplier_id, supplier_data)

    if supplier is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Supplier not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Supplier updated succesfully",
        "data" : supplier
    }

@router.delete(
    "/{supplier_id}",
    response_model=ResponseSchema[SupplierResponse]
)
def delete(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    supplier = delete_supplier(db, supplier_id)

    if supplier is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Supplier not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Supplier deleted succesfully",
        "data" : supplier
    }