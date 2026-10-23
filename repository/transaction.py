from sqlalchemy.orm import Session

from models.transaction import Transaction

def create(db: Session, transaction: Transaction) -> Transaction:
    db.add(transaction)
    db.flush()
    return transaction

def get_transaction_by_id(
    db: Session,
    transaction_id: int
) -> Transaction | None:
    return (
        db.query(Transaction)
        .filter(Transaction.id == transaction_id)
        .first()
    )

def get_transactions(
    db: Session
) -> list[Transaction]:
    return db.query(Transaction).all()

def get_some_transactions(
    db: Session,
    transaction_ids: list[int]
) -> list[Transaction]:
    return db.query(Transaction).filter(Transaction.id.in_(transaction_ids)).all()

def delete_transaction(
    db: Session,
    transaction: Transaction,
) -> None:
    db.delete(transaction)
    db.flush()
