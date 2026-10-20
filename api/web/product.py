from fastapi import APIRouter, Depends, status, UploadFile,Depends, File, Form, UploadFile, status
from core.exception import AppException
from sqlalchemy.orm import Session

from core.exception import AppException
from database.dependency import get_db
from schemas.common.respons import ResponseSchema
from schemas.common.product import (
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

from uuid import uuid4

from core.storage import upload_image


router = APIRouter(
    prefix="/api/products",
    tags=["products web"]
)

 
@router.post(
    "",
    response_model=ResponseSchema[ProductResponse],
    status_code=status.HTTP_201_CREATED
)
def create(
    name: str = Form(...),
    category_id: int = Form(...),
    unit_id: int = Form(...),
    sku: str = Form(...),
    unit_size: int = Form(...),
    sell_price: int = Form(...),
    upload_file: UploadFile=(...),
    db: Session = Depends(get_db)
):

    key = None

    if upload_file:
            if upload_file.content_type not in {
                "image/jpeg",
                "image/png",
                "image/webp",
            }:
                raise AppException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    message="The file must be an image"
                )

            key = f"images/{uuid4().hex}"

            if upload_file.content_type == "image/jpeg":
                key += ".jpg"
            elif upload_file.content_type == "image/png":
                key += ".png"
            else:
                key += ".webp"

            upload_image(upload_file.file, key, upload_file.content_type)

    product_data = ProductCreate(
        name=name,
        category_id=category_id,
        unit_id=unit_id,
        sku=sku,
        unit_size=unit_size,
        sell_price=sell_price,
    )

            
    product = create_product(db, product_data,key)

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
    name: str | None = Form(None),
    category_id: int | None = Form(None),
    unit_id: int | None = Form(None),
    sku: str | None = Form(None),
    unit_size: int | None = Form(None),
    sell_price: int | None = Form(None),
    upload_file: UploadFile | None = File(None),
    db: Session = Depends(get_db)
):

    if upload_file:
            if upload_file.content_type not in {
                "image/jpeg",
                "image/png",
                "image/webp",
            }:
                raise AppException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    message="The file must be an image"
                )

            key = f"images/{uuid4().hex}"

            if upload_file.content_type == "image/jpeg":
                key += ".jpg"
            elif upload_file.content_type == "image/png":
                key += ".png"
            else:
                key += ".webp"

            upload_image(upload_file.file, key, upload_file.content_type)

    product_data = ProductUpdate(
        name=name,
        category_id=category_id,
        unit_id=unit_id,
        sku=sku,
        unit_size=unit_size,
        sell_price=sell_price,
        image_key=key
    )

    product = update_product(
        db,
        product_id,
        product_data,
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