from fastapi import APIRouter, Depends, HTTPException, status
from core.exception import AppException
from sqlalchemy.orm import Session

from core.exception import AppException
from database.dependency import get_db
from schemas.respons import ResponseSchema
from schemas.category import (
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate,
)
from service.category import (
    create_category,
    get_category,
    get_categories,
    update_category,
    delete_category,
)


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.post(
    "",
    response_model=ResponseSchema[CategoryResponse],
    status_code=status.HTTP_201_CREATED
)
def create(
    category_data: CategoryCreate,
    db: Session = Depends(get_db)
):
    category = create_category(db, category_data)

    if category is None:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Failed to create category"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_201_CREATED,
        "message" : "category created succesfully",
        "data" : category
    }


@router.get(
    "",
    response_model=ResponseSchema[list[CategoryResponse]]
)
def get_all(
    db: Session = Depends(get_db)
):
    category = get_categories(db)

    if category is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Category not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "category retrieved succesfully",
        "data" : category
    }


@router.get(
    "/{category_id}",
    response_model=ResponseSchema[CategoryResponse]
)
def get_one(
    category_id: int,
    db: Session = Depends(get_db)
):
    category = get_category(db, category_id)

    if category is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Category not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "category retrieved succesfully",
        "data" : category
    }


@router.patch(
    "/{category_id}",
    response_model=ResponseSchema[CategoryResponse]
)
def update(
    category_id: int,
    category_data: CategoryUpdate,
    db: Session = Depends(get_db)
):
    category = update_category(
        db,
        category_id,
        category_data
    )

    if category is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Category not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "category updated succesfully",
        "data" : category
    }


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=ResponseSchema[CategoryResponse]
)
def delete(
    category_id: int,
    db: Session = Depends(get_db)
):
    category = delete_category(db, category_id)

    if category is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Category not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "category deleted succesfully",
        "data" : category
    }