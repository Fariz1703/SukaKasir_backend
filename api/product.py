from fastapi import APIRouter, Depends, HTTPException, status
from core.exception import AppException
from sqlalchemy.orm import Session

from core.exception import AppException
from database.dependency import get_db
from schemas.respons import ResponseSchema
from schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductUpdate,
)
from service.product import create_product
from service.product import (
    create_product,
    get_products,
    get_product,
    update_product,
    delete_product,
)


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post(
    "",
    response_model=ResponseSchema[ProductResponse],
    status_code=status.HTTP_201_CREATED
)
def create(
    product_data: ProductCreate,
    db: Session = Depends(get_db)
):
    product = create_product(db, product_data)

    if product is None:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Failed to create Product"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_201_CREATED,
        "message" : "Product created succesfully",
        "data" : product
    }


@router.get(
    "",
    response_model=ResponseSchema[list[ProductResponse]]
)
def get_all(
    db: Session = Depends(get_db)
):
    product = get_products(db)

    if product is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Product not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Product retrieved succesfully",
        "data" : product
    }


@router.get(
    "/{product_id}",
    response_model=ResponseSchema[ProductResponse]
)
def get_one(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = get_product(db, product_id)

    if product is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Product not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Product retrieved succesfully",
        "data" : product
    }


@router.patch(
    "/{product_id}",
    response_model=ResponseSchema[ProductResponse]
)
def update(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db)
):
    product = update_product(
        db,
        product_id,
        product_data
    )

    if product is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Product not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Product updated succesfully",
        "data" : product
    }


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=ResponseSchema[ProductResponse]
)
def delete(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = delete_product(db, product_id)

    if product is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Product not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Product deleted succesfully",
        "data" : product
    }