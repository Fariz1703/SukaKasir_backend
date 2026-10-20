from fastapi import APIRouter, Depends, status
from core.exception import AppException
from sqlalchemy.orm import Session

from core.exception import AppException
from database.dependency import get_db
from schemas.common.respons import ResponseSchema
from schemas.common.transactionType import (
    TransactionTypeCreate,
    TransactionTypeResponse,
    TransactionTypeUpdate,
)
from service.transactionType import (
    create_TransactionType,
    get_TransactionType,
    get_TransactionTypes,
    update_TransactionType,
    delete_TransactionType,
)


router = APIRouter(
    prefix="/api/web/transaction_types",
    tags=["transaction_types Web"]
)


@router.post(
    "",
    response_model=ResponseSchema[TransactionTypeResponse],
    status_code=status.HTTP_201_CREATED
)
def create(
    transaction_type_data: TransactionTypeCreate,
    db: Session = Depends(get_db)
):
    transactionType = create_TransactionType(db, transaction_type_data)

    if transactionType is None:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Failed to create transactionType"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_201_CREATED,
        "message" : "transactionType created succesfully",
        "data" : transactionType
    }


@router.get(
    "",
    response_model=ResponseSchema[list[TransactionTypeResponse]]
)
def get_all(
    db: Session = Depends(get_db)
):
    transactionType = get_TransactionTypes(db)

    if transactionType is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="transactionType not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "transactionType retrieved succesfully",
        "data" : transactionType
    }


@router.get(
    "/{transaction_type_id}",
    response_model=ResponseSchema[TransactionTypeResponse]
)
def get_one(
    transaction_type_id: int,
    db: Session = Depends(get_db)
):
    transactionType = get_TransactionType(db, transaction_type_id)

    if transactionType is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="transactionType not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "transactionType retrieved succesfully",
        "data" : transactionType
    }


@router.patch(
    "/{transaction_type_id}",
    response_model=ResponseSchema[TransactionTypeResponse]
)
def update(
    transaction_type_id: int,
    transaction_type_data: TransactionTypeUpdate,
    db: Session = Depends(get_db)
):
    transactionType = update_TransactionType(
        db,
        transaction_type_id,
        transaction_type_data
    )

    if transactionType is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="transactionType not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "transactionType updated succesfully",
        "data" : transactionType
    }


@router.delete(
    "/{transaction_type_id}",
    status_code=status.HTTP_200_OK,
    response_model=ResponseSchema[TransactionTypeResponse]
)
def delete(
    transaction_type_id: int,
    db: Session = Depends(get_db)
):
    transactionType = delete_TransactionType(db, transaction_type_id)

    if transactionType is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="transactionType not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "transactionType deleted succesfully",
        "data" : transactionType
    }