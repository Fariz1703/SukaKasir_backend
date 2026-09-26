from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TransactionBase(BaseModel):
    transaction_type_id : int

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id : int
    created_at:datetime
    updated_at:datetime

    model_config = ConfigDict(from_attributes=True)

class TransactionUpdate(BaseModel):
    transaction_type_id: int | None = None