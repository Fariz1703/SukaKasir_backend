from sqlalchemy.orm import Session

from core.exception import AppException
from models.transaction import Transaction
from schemas.transaction import TransactionCreate, TransactionUpdate
from service.transactionType import get_TransactionType


def create_transaction(
    db: Session,
    Transaction_data: TransactionCreate
) -> Transaction:


    transaction = Transaction(
        transaction_type_id=Transaction_data.transaction_type_id,
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction

def get_transaction(
    db: Session,
    Transaction_id: int
) -> Transaction | None:

    return (
        db.query(Transaction)
        .filter(Transaction.id == Transaction_id)
        .first()
    )

def get_transactions(
    db: Session
) -> list[Transaction]:

    return db.query(Transaction).all()

def get_transaction(
    db: Session,
    Transaction_id: int
) -> Transaction | None:

    return (
        db.query(Transaction)
        .filter(Transaction.id == Transaction_id)
        .first()
    )


def get_transactions(
    db: Session
) -> list[Transaction]:

    return db.query(Transaction).all()


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

    db.commit()
    db.refresh(transaction)

    return transaction


def delete_transaction(
    db: Session,
    Transaction_id: int
) -> Transaction | None:

    Transaction = get_transaction(db, Transaction_id)

    if Transaction is None:
        return None

    db.delete(Transaction)
    db.commit()

    return Transaction