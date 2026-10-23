from sqlalchemy.orm import Session

from models.transactionItem import TransactionItem

def create(db: Session, transaction_item: TransactionItem) -> TransactionItem:
    db.add(transaction_item)
    db.flush()
    return transaction_item

def get_transaction_item_by_id(
    db: Session,
    transaction_item_id: int
) -> TransactionItem | None:
    return (
        db.query(TransactionItem)
        .filter(TransactionItem.id == transaction_item_id)
        .first()
    )

def get_transaction_items(
    db: Session
) -> list[TransactionItem]:
    return db.query(TransactionItem).all()

def get_some_transaction_items(
    db: Session,
    transaction_item_ids: list[int]
) -> list[TransactionItem]:
    return db.query(TransactionItem).filter(TransactionItem.id.in_(transaction_item_ids)).all()

def delete_transaction_item(
    db: Session,
    transaction_item: TransactionItem,
) -> None:
    db.delete(transaction_item)
    db.flush()
