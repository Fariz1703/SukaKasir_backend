from fastapi import APIRouter, Depends, HTTPException, status
from core.exception import AppException
from sqlalchemy.orm import Session

from core.exception import AppException
from database.dependency import get_db
from schemas.respons import ResponseSchema
from schemas.transaction import (
    TransactionCreate,
    TransactionResponse,
    TransactionUpdate,
)
from service.transaction import (
    create_transaction,
    get_transaction,
    get_transactions,
    update_transaction,
    delete_transaction,
)


router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)


@router.post(
    "",
    response_model=ResponseSchema[TransactionResponse],
    status_code=status.HTTP_201_CREATED
)
def create(
    transaction_data: TransactionCreate,
    db: Session = Depends(get_db)
):
    transaction = create_transaction(db, transaction_data)

    if transaction is None:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Failed to create transaction"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_201_CREATED,
        "message" : "transaction created succesfully",
        "data" : transaction
    }


@router.get(
    "",
    response_model=ResponseSchema[list[TransactionResponse]]
)
def get_all(
    db: Session = Depends(get_db)
):
    transaction = get_transactions(db)

    if transaction is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="transaction not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "transaction retrieved succesfully",
        "data" : transaction
    }


@router.get(
    "/{transaction__id}",
    response_model=ResponseSchema[TransactionResponse]
)
def get_one(
    transaction__id: int,
    db: Session = Depends(get_db)
):
    transaction = get_transaction(db, transaction__id)

    if transaction is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="transaction not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "transaction retrieved succesfully",
        "data" : transaction
    }


@router.patch(
    "/{transaction__id}",
    response_model=ResponseSchema[TransactionResponse]
)
def update(
    transaction__id: int,
    transaction__data: TransactionUpdate,
    db: Session = Depends(get_db)
):
    transaction = update_transaction(
        db,
        transaction__id,
        transaction__data
    )

    if transaction is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="transaction not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "transaction updated succesfully",
        "data" : transaction
    }


@router.delete(
    "/{transaction__id}",
    status_code=status.HTTP_200_OK,
    response_model=ResponseSchema[TransactionResponse]
)
def delete(
    transaction__id: int,
    db: Session = Depends(get_db)
):
    transaction = delete_transaction(db, transaction__id)

    if transaction is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="transaction not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "transaction deleted succesfully",
        "data" : transaction
    }