from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProductBase(BaseModel):
    category_id : int
    name : str
    unit_id : int
    sku : str
    unit_size : int
    sell_price : int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id : int
    created_at:datetime
    updated_at:datetime

    model_config = ConfigDict(from_attributes=True)

class ProductUpdate(BaseModel):
    category_id : int | None = None
    name : str | None = None
    unit_id : int | None = None
    sku : str | None = None
    unit_size : int | None = None
    sell_price : int | None = None