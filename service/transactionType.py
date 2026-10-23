from sqlalchemy.orm import Session
from fastapi import status

from core.exception import AppException
from repository import transactionType as transaction_type_repository
from models.transactionType import TransactionType
from schemas.common.transactionType import TransactionTypeCreate, TransactionTypeUpdate


def create_TransactionType(
    db: Session,
    transactionTypeData: TransactionTypeCreate
) -> TransactionType:

    transactionType = TransactionType(
        name=transactionTypeData.name,
        description=transactionTypeData.description,
        need_supplier=transactionTypeData.need_supplier
    )

    try:
        transaction_type_repository.create(db, transactionType)
        db.commit()
        db.refresh(transactionType)
        return transactionType
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to create transaction type",
        ) from exc


def get_TransactionType(
    db: Session,
    TransactionType_id: int
) -> TransactionType | None:

    return transaction_type_repository.get_transaction_type_by_id(db, TransactionType_id)


def get_TransactionTypes(
    db: Session
) -> list[TransactionType]:

    return transaction_type_repository.get_transaction_types(db)


def update_TransactionType(
    db: Session,
    TransactionType_id: int,
    TransactionType_data: TransactionTypeUpdate
) -> TransactionType | None:

    transactionType = get_TransactionType(db, TransactionType_id)

    if transactionType is None:
        return None

    if TransactionType_data.name is not None:
        transactionType.name = TransactionType_data.name

    if TransactionType_data.description is not None:
        transactionType.description = TransactionType_data.description

    if TransactionType_data.need_supplier is not None:
        transactionType.need_supplier = TransactionType_data.need_supplier

    try:
        db.commit()
        db.refresh(transactionType)
        return transactionType

    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to update transaction type",
        ) from exc


def delete_TransactionType(
    db: Session,
    TransactionType_id: int
) -> TransactionType | None:

    transactionType = get_TransactionType(db, TransactionType_id)

    if transactionType is None:
        return None

    try:
        transaction_type_repository.delete_transaction_type(db, transactionType)
        db.commit()
        db.refresh(transactionType)
        return transactionType

    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to update transaction type",
        ) from exc