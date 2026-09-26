from sqlalchemy.orm import Session

from models.transactionType import TransactionType
from schemas.transactionType import TransactionTypeCreate, TransactionTypeUpdate


def create_TransactionType(
    db: Session,
    transactionTypeData: TransactionTypeCreate
) -> TransactionType:

    transactionType = TransactionType(
        name=transactionTypeData.name,
        description=transactionTypeData.description,
        need_supplier=transactionTypeData.need_supplier
    )

    db.add(transactionType)
    db.commit()
    db.refresh(transactionType)

    return transactionType

def get_TransactionType(
    db: Session,
    TransactionType_id: int
) -> TransactionType | None:

    return (
        db.query(TransactionType)
        .filter(TransactionType.id == TransactionType_id)
        .first()
    )


def get_TransactionTypes(
    db: Session
) -> list[TransactionType]:

    return db.query(TransactionType).all()


def update_TransactionType(
    db: Session,
    TransactionType_id: int,
    TransactionType_data: TransactionTypeUpdate
) -> TransactionType | None:

    TransactionType = get_TransactionType(db, TransactionType_id)

    if TransactionType is None:
        return None

    if TransactionType_data.name is not None:
        TransactionType.name = TransactionType_data.name

    if TransactionType_data.description is not None:
        TransactionType.description = TransactionType_data.description

    if TransactionType_data.need_supplier is not None:
        TransactionType.need_supplier = TransactionType_data.need_supplier

    db.commit()
    db.refresh(TransactionType)

    return TransactionType


def delete_TransactionType(
    db: Session,
    TransactionType_id: int
) -> TransactionType | None:

    TransactionType = get_TransactionType(db, TransactionType_id)

    if TransactionType is None:
        return None

    db.delete(TransactionType)
    db.commit()

    return TransactionType