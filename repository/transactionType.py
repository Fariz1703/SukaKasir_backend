from sqlalchemy.orm import Session

from models.transactionType import TransactionType

def create(db: Session, transaction_type: TransactionType) -> TransactionType:
    db.add(transaction_type)
    db.flush()
    return transaction_type

def get_transaction_type_by_id(
    db: Session,
    transaction_type_id: int
) -> TransactionType | None:
    return (
        db.query(TransactionType)
        .filter(TransactionType.id == transaction_type_id)
        .first()
    )

def get_transaction_types(
    db: Session
) -> list[TransactionType]:
    return db.query(TransactionType).all()

def get_some_transaction_types(
    db: Session,
    transaction_type_ids: list[int]
) -> list[TransactionType]:
    return db.query(TransactionType).filter(TransactionType.id.in_(transaction_type_ids)).all()

def delete_transaction_type(
    db: Session,
    transaction_type: TransactionType,
) -> None:
    db.delete(transaction_type)
    db.flush()
