from pydantic import BaseModel


# Data item yang dikirim client
class CreateTransactionItem(BaseModel):
    quantity: int
    product_supplier_id: int | None = None
    product_id: int


# Request untuk membuat transaksi
class CreateTransactionCreate(BaseModel):
    transaction_type_id: int
    items: list[CreateTransactionItem]


# Satu item dalam response
class TransactionItemResponse(BaseModel):
    product_id: int
    product_supplier_id: int | None = None
    unit_price: float
    quantity: int


# Response transaksi
class CreateTransactionResponse(BaseModel):
    transaction_id: int
    items: list[TransactionItemResponse]