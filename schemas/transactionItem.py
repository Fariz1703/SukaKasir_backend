from pydantic import BaseModel, ConfigDict
from datetime import datetime
from schemas.product import ProductResponse

class TransactionItemBase(BaseModel):
    
    transaction_id: int
    quantity: int


class TransactionItemCreate(TransactionItemBase):
    product_supplier_id: int | None = None
    product_id: int | None = None


class TransactionItemResponse(TransactionItemBase):
    id: int
    product_supplier_id: int | None = None
    product_id: int 

    model_config = ConfigDict(from_attributes=True)


class TransactionItemUpdate(BaseModel):
    product_id: int | None = None
    product_supplier_id: int | None = None
    transaction_id: int | None = None
    quantity: int | None = None
    unit_price: int | None = None