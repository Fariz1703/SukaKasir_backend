from sqlalchemy.orm import Session
from fastapi import status

from core.exception import AppException
from models.transaction import Transaction
from models.transactionItem import TransactionItem
from schemas.transactionItem import TransactionItemCreate, TransactionItemUpdate
from service.product import get_some_product,get_product
from service.productSupplier import get_product_supplier
from service.transactionType import get_TransactionType
from service.transaction import get_transaction

def create_transaction_item_out(
    db: Session,
    transaction_item_data: TransactionItemCreate,
) -> TransactionItem:

    product = get_product(
        db,
        transaction_item_data.product_id
    )

    if product is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message=f"Product with id {transaction_item_data.product_id} not found"
        )

    transaction_item = TransactionItem(
        product_id=product.id,
        transaction_id=transaction_item_data.transaction_id,
        unit_price=product.sell_price,
        quantity=transaction_item_data.quantity,
    )

    db.add(transaction_item)
    db.commit()
    db.refresh(transaction_item)

    return transaction_item

def create_transaction_item_in(
    db: Session,
    transaction_item_data: TransactionItemCreate,
) -> TransactionItem:

    product_supplier = get_product_supplier(
        db,
        transaction_item_data.product_supplier_id
    )

    if product_supplier is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message=f"Product with id {transaction_item_data.product_id} not found"
        )

    transaction_item = TransactionItem(
        product_id=product_supplier.product_id,
        transaction_id=transaction_item_data.transaction_id,
        quantity=transaction_item_data.quantity,
        unit_price=product_supplier.buy_price,
        product_supplier_id=transaction_item_data.product_supplier_id
    )

    db.add(transaction_item)
    db.commit()
    db.refresh(transaction_item)

    return transaction_item

def create_transaction_item_switch(
        db: Session, 
        transaction_item_data: TransactionItemCreate
) -> TransactionItem:
    get_transaction_item = get_transaction(
        db,
        transaction_item_data.transaction_id
    )   
    
    get_transaction_type_item = get_TransactionType(
        db,
        get_transaction_item.transaction_type_id
    )

    if get_transaction_type_item.need_supplier is True:
        if transaction_item_data.product_supplier_id is None:
            raise AppException(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Product supplier id is required for this transaction type."
            )

        return create_transaction_item_in(db, transaction_item_data)
    else:
        if transaction_item_data.product_supplier_id is not None:
            raise AppException(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Product supplier id is not allowed for this transaction type."
            )
        return create_transaction_item_out(db, transaction_item_data)


def validate_transaction_item_by_transaction_type(
    db: Session,
    transaction_id: int,
    product_supplier_id: int | None,
) -> None:
    transaction = get_transaction(db, transaction_id)

    if transaction is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message=f"Transaction with id {transaction_id} not found"
        )

    transaction_type = get_TransactionType(
        db,
        transaction.transaction_type_id
    )

    if transaction_type.need_supplier is True:
        if product_supplier_id is None:
            raise AppException(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Product supplier id is required for this transaction type."
            )
    else:
        if product_supplier_id is not None:
            raise AppException(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Product supplier id is not allowed for this transaction type."
            )


def get_transaction_item(
    db: Session,
    Transaction_item_id: int
) -> TransactionItem | None:

    return (
        db.query(TransactionItem)
        .filter(TransactionItem.id == Transaction_item_id)
        .first()
    )


def get_transaction_items(
    db: Session
) -> list[TransactionItem]:

    return db.query(TransactionItem).all()


def update_transaction_item_out(
    db: Session,
    transaction_item_id: int,
    transaction_item_data: TransactionItemUpdate,
) -> TransactionItem | None:
    transaction_item = get_transaction_item(
        db,
        transaction_item_id,
    )

    if transaction_item is None:
        return None

    if transaction_item_data.product_id is not None:
        product = get_product(
            db,
            transaction_item_data.product_id,
        )

        if product is None:
            raise AppException(
                status_code=status.HTTP_404_NOT_FOUND,
                message=f"Product with id {transaction_item_data.product_id} not found",
            )

        transaction_item.product_id = product.id

    if transaction_item_data.transaction_id is not None:
        transaction = get_transaction(
            db,
            transaction_item_data.transaction_id,
        )

        if transaction is None:
            raise AppException(
                status_code=status.HTTP_404_NOT_FOUND,
                message=f"Transaction with id {transaction_item_data.transaction_id} not found",
            )

        transaction_item.transaction_id = transaction.id

    if transaction_item_data.quantity is not None:
        transaction_item.quantity = transaction_item_data.quantity

    if transaction_item_data.unit_price is not None:
        transaction_item.unit_price = transaction_item_data.unit_price

    target_transaction_id = (
        transaction_item_data.transaction_id
        if transaction_item_data.transaction_id is not None
        else transaction_item.transaction_id
    )
    target_product_supplier_id = (
        transaction_item_data.product_supplier_id
        if transaction_item_data.product_supplier_id is not None
        else transaction_item.product_supplier_id
    )

    validate_transaction_item_by_transaction_type(
        db,
        target_transaction_id,
        target_product_supplier_id,
    )

    db.commit()
    db.refresh(transaction_item)

    return transaction_item


def update_transaction_item_in(
    db: Session,
    transaction_item_id: int,
    transaction_item_data: TransactionItemUpdate,
) -> TransactionItem | None:
    transaction_item = get_transaction_item(
        db,
        transaction_item_id,
    )

    if transaction_item is None:
        return None

    if transaction_item_data.product_supplier_id is not None:
        product_supplier = get_product_supplier(
            db,
            transaction_item_data.product_supplier_id,
        )

        if product_supplier is None:
            raise AppException(
                status_code=status.HTTP_404_NOT_FOUND,
                message=f"Product supplier with id {transaction_item_data.product_supplier_id} not found",
            )

        transaction_item.product_id = product_supplier.product_id
        transaction_item.product_supplier_id = product_supplier.id

    if transaction_item_data.transaction_id is not None:
        transaction = get_transaction(
            db,
            transaction_item_data.transaction_id,
        )

        if transaction is None:
            raise AppException(
                status_code=status.HTTP_404_NOT_FOUND,
                message=f"Transaction with id {transaction_item_data.transaction_id} not found",
            )

        transaction_item.transaction_id = transaction.id

    if transaction_item_data.quantity is not None:
        transaction_item.quantity = transaction_item_data.quantity

    if transaction_item_data.unit_price is not None:
        transaction_item.unit_price = transaction_item_data.unit_price

    target_transaction_id = (
        transaction_item_data.transaction_id
        if transaction_item_data.transaction_id is not None
        else transaction_item.transaction_id
    )
    target_product_supplier_id = (
        transaction_item_data.product_supplier_id
        if transaction_item_data.product_supplier_id is not None
        else transaction_item.product_supplier_id
    )

    validate_transaction_item_by_transaction_type(
        db,
        target_transaction_id,
        target_product_supplier_id,
    )

    db.commit()
    db.refresh(transaction_item)

    return transaction_item


def update_transaction_item_switch(
        db: Session, 
        transaction_item_id: int, 
        transaction_item_data: TransactionItemUpdate
) -> TransactionItem | None:

    get_transaction_item = get_transaction(
        db,
        transaction_item_data.transaction_id
    )   
    
    get_transaction_type_item = get_TransactionType(
        db,
        get_transaction_item.transaction_type_id
    )
    if get_transaction_type_item.need_supplier is True:
        return update_transaction_item_in(db, transaction_item_id, transaction_item_data)
    else:
        return update_transaction_item_out(db, transaction_item_id, transaction_item_data)

def delete_transaction_item(
    db: Session,
    Transaction_id: int
) -> Transaction | None:

    Transaction = get_transaction(db, Transaction_id)

    if Transaction is None:
        return None

    db.delete(Transaction)
    db.commit()

    return Transaction