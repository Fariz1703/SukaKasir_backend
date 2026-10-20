from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProductSupplierBase(BaseModel):
    product_id : int
    supplier_id : int
    buy_price : int

class ProductSupplierCreate(ProductSupplierBase):
    pass

class ProductSupplierResponse(ProductSupplierBase):
    id : int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ProductSupplierUpdate(BaseModel):
    product_id : int | None = None
    supplier_id : int | None = None
    buy_price : int | None = None