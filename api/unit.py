from fastapi import APIRouter, Depends, HTTPException, status
from core.exception import AppException
from sqlalchemy.orm import Session

from core.exception import AppException
from database.dependency import get_db
from schemas.respons import ResponseSchema
from schemas.unit import (
    UnitCreate,
    UnitResponse,
    UnitUpdate,
)
from service.unit import (
    create_unit,
    get_unit,
    get_units,
    update_unit,
    delete_unit,
)


router = APIRouter(
    prefix="/units",
    tags=["Units"]
)


@router.post(
    "",
    response_model=ResponseSchema[UnitResponse],
    status_code=status.HTTP_201_CREATED
)
def create(
    Unit_data: UnitCreate,
    db: Session = Depends(get_db)
):
    Unit = create_unit(db, Unit_data)

    if Unit is None:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Failed to create Unit"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_201_CREATED,
        "message" : "Unit created succesfully",
        "data" : Unit
    }


@router.get(
    "",
    response_model=ResponseSchema[list[UnitResponse]]
)
def get_all(
    db: Session = Depends(get_db)
):
    Unit = get_units(db)

    if Unit is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Unit not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Unit retrieved succesfully",
        "data" : Unit
    }


@router.get(
    "/{Unit_id}",
    response_model=ResponseSchema[UnitResponse]
)
def get_one(
    Unit_id: int,
    db: Session = Depends(get_db)
):
    Unit = get_unit(db, Unit_id)

    if Unit is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Unit not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Unit retrieved succesfully",
        "data" : Unit
    }


@router.patch(
    "/{Unit_id}",
    response_model=ResponseSchema[UnitResponse]
)
def update(
    Unit_id: int,
    Unit_data: UnitUpdate,
    db: Session = Depends(get_db)
):
    Unit = update_unit(
        db,
        Unit_id,
        Unit_data
    )

    if Unit is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Unit not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Unit updated succesfully",
        "data" : Unit
    }


@router.delete(
    "/{Unit_id}",
    status_code=status.HTTP_200_OK,
    response_model=ResponseSchema[UnitResponse]
)
def delete(
    Unit_id: int,
    db: Session = Depends(get_db)
):
    Unit = delete_unit(db, Unit_id)

    if Unit is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Unit not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Unit deleted succesfully",
        "data" : Unit
    }