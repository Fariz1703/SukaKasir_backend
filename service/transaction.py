from sqlalchemy.orm import Session  
from fastapi import status

from core.exception import AppException
from repository import transaction as transaction_repository
from models.transaction import Transaction
from schemas.common.transaction import TransactionCreate, TransactionUpdate
from service.transactionType import get_TransactionType


def create_transaction(
    db: Session,
    Transaction_data: TransactionCreate
) -> Transaction:


    transaction = Transaction(
        transaction_type_id=Transaction_data.transaction_type_id,
    )

    try:
        transaction_repository.create(db, transaction)
        db.commit()
        db.refresh(transaction)
        return transaction

    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to create supplier",
        ) from exc

def get_transaction(
    db: Session,
    Transaction_id: int
) -> Transaction | None:

    return transaction_repository.get_transaction_by_id(db, Transaction_id)

def get_transactions(
    db: Session
) -> list[Transaction]:

    return transaction_repository.get_transactions(db)

def get_transaction(
    db: Session,
    Transaction_id: int
) -> Transaction | None:

    return transaction_repository.get_transaction_by_id(db, Transaction_id)



def update_transaction(
    db: Session,
    transaction_id: int,
    transaction_data: TransactionUpdate
) -> Transaction | None:

    transaction = get_transaction(db, transaction_id)

    if transaction is None:
        return None

    if transaction_data.transaction_type_id is not None:
        transaction.transaction_type_id = transaction_data.transaction_type_id

    try:
        db.commit()
        db.refresh(transaction)
        return transaction

    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to update transaction",
        ) from exc


def delete_transaction(
    db: Session,
    Transaction_id: int
) -> Transaction | None:

    transaction = get_transaction(db, Transaction_id)

    if Transaction is None:
        return None

    try:
        transaction_repository.delete_transaction(db, transaction)
        db.commit()
        return transaction

    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to delete transaction",
        ) from exc