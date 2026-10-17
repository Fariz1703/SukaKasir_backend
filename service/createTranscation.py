from sqlalchemy.orm import Session

from models.product import Product
from models.productSupplier import ProductSupplier
from models.transactionItem import TransactionItem
from service.transaction import create_transaction
from service.transactionItem import create_transaction_item_switch
from service.product import get_product
from schemas.transaction import (
    TransactionCreate,
    
)
from schemas.transactionItem import TransactionItemCreate
from schemas.createTransaction import CreateTransactionCreate,CreateTransactionResponse,TransactionItemResponse

def CreateCreateTransaction(
    db: Session,
    transcation_data: CreateTransactionCreate
) -> CreateTransactionResponse:


    payload = TransactionCreate(transaction_type_id=transcation_data.transaction_type_id)
    
    TransactionNumber = create_transaction(
           db=db,
           Transaction_data=payload
    )
    
    transaction_items = []

    for item in transcation_data.items:

        product = get_product(
        db,
        item.product_id
        )

        transaction_item=TransactionItemCreate(
            transaction_id=TransactionNumber.id,
            product_id=product.id,
            product_supplier_id=item.product_supplier_id,
            unit_price=product.sell_price,
            quantity=item.quantity,
        ) 

        saved_item = create_transaction_item_switch(
            db=db,
            transaction_item_data=transaction_item         
        )


        item_response = TransactionItemResponse(
            product_id=saved_item.product_id,
            product_supplier_id=saved_item.product_supplier_id,
            unit_price=saved_item.unit_price,
            quantity=saved_item.quantity,
        )

        transaction_items.append(item_response)

    return CreateTransactionResponse(
        transaction_id = TransactionNumber.id,
        items=transaction_items
    )







