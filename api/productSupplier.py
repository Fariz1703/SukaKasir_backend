from fastapi import APIRouter, Depends, HTTPException, status
from core.exception import AppException
from sqlalchemy.orm import Session

from core.exception import AppException
from database.dependency import get_db
from schemas.respons import ResponseSchema
from schemas.productSupplier import (
    ProductSupplierCreate,
    ProductSupplierResponse,
    ProductSupplierUpdate,
)
from service.productSupplier import (
    create_product_supplier,
    get_product_suppliers,
    get_product_supplier,
    update_product_supplier,
    delete_product_supplier,
)

router = APIRouter(
    prefix="/product_suppliers",
    tags=["Product_Suppliers"]
)

@router.post(
    "",
    response_model=ResponseSchema[ProductSupplierResponse],
    status_code=status.HTTP_201_CREATED
)
def create(
    product_supplier_data: ProductSupplierCreate,
    db: Session = Depends(get_db)
):
    product_supplier = create_product_supplier(db, product_supplier_data)

    if product_supplier is None:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Failed to create Product Supplier"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_201_CREATED,
        "message" : "Product Supplier created succesfully",
        "data" : product_supplier
    }

@router.get(
    "",
    response_model=ResponseSchema[list[ProductSupplierResponse]]
)
def get_all(
    db: Session = Depends(get_db)
):
    product_suppliers = get_product_suppliers(db)

    if product_suppliers is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Product Suppliers not found"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Product Suppliers retrieved succesfully",
        "data" : product_suppliers
    }

@router.get(
    "/{product_supplier_id}",
    response_model=ResponseSchema[ProductSupplierResponse]
)
def get(
    product_supplier_id: int,
    db: Session = Depends(get_db)
):
    product_supplier = get_product_supplier(db, product_supplier_id)

    if product_supplier is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Product Supplier not found"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Product Supplier retrieved succesfully",
        "data" : product_supplier
    }

@router.patch(
    "/{product_supplier_id}",
    response_model=ResponseSchema[ProductSupplierResponse]
)
def update(
    product_supplier_id: int,
    product_supplier_data: ProductSupplierUpdate,
    db: Session = Depends(get_db)
):
    product_supplier = update_product_supplier(db, product_supplier_id, product_supplier_data)

    if product_supplier is None:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Failed to update Product Supplier"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Product Supplier updated succesfully",
        "data" : product_supplier
    }

router.delete(
    "/{product_supplier_id}",
    status_code=status.HTTP_200_OK,
    response_model=ResponseSchema[ProductSupplierResponse]
)
def delete(
    product_supplier_id: int,
    db: Session = Depends(get_db)
):
    product_supplier = delete_product_supplier(db, product_supplier_id)

    if product_supplier is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Product Supplier not found"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Product Supplier deleted succesfully",
        "data" : product_supplier
    }