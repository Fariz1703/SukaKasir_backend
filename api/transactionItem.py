from fastapi import APIRouter, Depends, HTTPException, status
from core.exception import AppException
from sqlalchemy.orm import Session

from core.exception import AppException
from database.dependency import get_db
from schemas.respons import ResponseSchema
from schemas.transactionItem import (
    TransactionItemCreate,
    TransactionItemResponse,
    TransactionItemUpdate,
)
from service.transactionItem import (
    create_transaction_item_switch,
    update_transaction_item_switch,
    get_transaction_item,
    get_transaction_items,
    delete_transaction_item,
)



router = APIRouter(
    prefix="/transaction_items",
    tags=["transaction_items"]
)


@router.post(
    "",
    response_model=ResponseSchema[TransactionItemResponse],
    status_code=status.HTTP_201_CREATED
)
def create(
    transaction_data: TransactionItemCreate,
    db: Session = Depends(get_db)
):
    transaction = create_transaction_item_switch(db, transaction_data)

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
    response_model=ResponseSchema[list[TransactionItemResponse]]
)
def get_all(
    db: Session = Depends(get_db)
):
    transaction = get_transaction_items(db)

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
    response_model=ResponseSchema[TransactionItemResponse]
)
def get_one(
    transaction__id: int,
    db: Session = Depends(get_db)
):
    transaction = get_transaction_item(db, transaction__id)

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
    response_model=ResponseSchema[TransactionItemResponse]
)
def update(
    transaction__id: int,
    transaction__data: TransactionItemUpdate,
    db: Session = Depends(get_db)
):
    transaction = update_transaction_item_switch(
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
    response_model=ResponseSchema[TransactionItemResponse]
)
def delete(
    transaction__id: int,
    db: Session = Depends(get_db)
):
    transaction = delete_transaction_item(db, transaction__id)

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