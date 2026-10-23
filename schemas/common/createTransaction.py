from pydantic import BaseModel


class CreateTransactionItem(BaseModel):
    quantity: int
    product_supplier_id: int | None = None
    product_id: int


class CreateTransactionCreate(BaseModel):
    transaction_type_id: int
    items: list[CreateTransactionItem]


class TransactionItemResponse(BaseModel):
    product_id: int
    product_supplier_id: int | None = None
    unit_price: float
    quantity: int


class CreateTransactionResponse(BaseModel):
    transaction_id: int
    items: list[TransactionItemResponse]