from sqlalchemy.orm import Session
from fastapi import status

from core.exception import AppException
from models.product import Product
from models.transaction import Transaction
from models.transactionItem import TransactionItem
from schemas.common.transactionItem import TransactionItemCreate, TransactionItemUpdate
from service.product import update_product
from repository import transactionItem as transaction_item_repository
from repository import product as product_repository
from repository import transaction as transaction_repository
from repository import productSupplier as product_supplier_repository 
from repository import transactionType as transaction_type_repository
from repository import transactionItem as transaction_item_repository

def create_transaction_item_out(
    db: Session,
    transaction_item_data: TransactionItemCreate,
) -> TransactionItem:

    product = product_repository.get_product_by_id(
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

    

    new_product_quantity =Product(stock=product.stock - transaction_item_data.quantity)

    if new_product_quantity.stock < 0:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message=f"Product with id {product.id} has insufficient stock"
        )

    update_product(
        db,
        product.id,
        product_data=new_product_quantity
    )

    try:
        transaction_item_repository.create(db, transaction_item)
        db.commit()
        db.refresh(transaction_item)
        return transaction_item
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to create transaction item",
        ) from exc


def create_transaction_item_in(
    db: Session,
    transaction_item_data: TransactionItemCreate,
) -> TransactionItem:

    product_supplier = product_supplier_repository.get_product_supplier_by_id(
        db,
        transaction_item_data.product_supplier_id
    )

    product = product_repository.get_product_by_id(
        db,
        transaction_item_data.product_id
    )

    if product_supplier is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message=f"Product with id {transaction_item_data.product_id} not found"
        )

    if transaction_item_data.quantity <= 0:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Quantity must be greater than zero"
        )

    new_product_quantity =Product(stock=product.stock + transaction_item_data.quantity)

    update_product(
        db,
        product.id,
        product_data=new_product_quantity
    )


    transaction_item = TransactionItem(
        product_id=product_supplier.product_id,
        transaction_id=transaction_item_data.transaction_id,
        quantity=transaction_item_data.quantity,
        unit_price=product_supplier.buy_price,
        product_supplier_id=transaction_item_data.product_supplier_id
    )

    try:
        transaction_item_repository.create(db, transaction_item)
        db.commit()
        db.refresh(transaction_item)
        return transaction_item
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to create transaction item",
        ) from exc


def create_transaction_item_switch(
        db: Session, 
        transaction_item_data: TransactionItemCreate
) -> TransactionItem:
    get_transaction_item = product_repository.get_product_by_id(
        db,
        transaction_item_data.transaction_id
    )   
    
    get_transaction_type_item = transaction_type_repository.get_transaction_type_by_id(
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
    transaction = transaction_repository.get_transaction_by_id(db, transaction_id)

    if transaction is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message=f"Transaction with id {transaction_id} not found"
        )

    transaction_type = transaction_type_repository.get_transaction_type_by_id(
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

    return transaction_item_repository.get_transaction_item_by_id(db, Transaction_item_id)


def get_transaction_items(
    db: Session
) -> list[TransactionItem]:

    return transaction_item_repository.get_transaction_items(db)


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
        product = product_repository.get_product_by_id(
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
        transaction = transaction_repository.get_transaction_by_id(
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

    try:
        db.commit()
        return transaction_item
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to create transaction item",
        ) from exc



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
        product_supplier = product_supplier_repository.get_product_supplier_by_id(
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
        transaction = transaction_repository.get_transaction_by_id(
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

    try:
        db.commit()
        return transaction_item
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to update transaction item",
        ) from exc



def update_transaction_item_switch(
        db: Session, 
        transaction_item_id: int, 
        transaction_item_data: TransactionItemUpdate
) -> TransactionItem | None:

    get_transaction_item = transaction_repository.get_transaction_by_id(
        db,
        transaction_item_data.transaction_id
    )   
    
    get_transaction_type_item = transaction_type_repository.get_transaction_type_by_id(
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

    transaction_item = transaction_item_repository.get_transaction_item_by_id(
        db,
        Transaction_id
    )

    if transaction_item is None:
        return None

    try:
        transaction_item_repository.delete_transaction_item(db, transaction_item)
        db.commit()
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to delete transaction item",
        ) from exc

    return transaction_item