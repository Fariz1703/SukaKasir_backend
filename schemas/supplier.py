from pydantic import BaseModel, ConfigDict
from datetime import datetime

class SupplierBase(BaseModel):
    name : str
    description : str

class SupplierCreate(SupplierBase):
    pass

class SupplierResponse(SupplierBase):
    id : int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SupplierUpdate(BaseModel):
    name : str | None = None
    description : str | None = None