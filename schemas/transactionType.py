from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TransactionType(BaseModel):
    name : str
    description : str
    need_supplier: bool

class TransactionTypeCreate(TransactionType):
    pass

class TransactionTypeResponse(TransactionType):
    id : int
    created_at:datetime
    updated_at:datetime

    model_config = ConfigDict(from_attributes=True)

class TransactionTypeUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    need_supplier: bool | None = None
