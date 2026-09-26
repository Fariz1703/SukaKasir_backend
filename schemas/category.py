from pydantic import BaseModel, ConfigDict
from datetime import datetime

class CategoryBase(BaseModel):
    name : str
    description : str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id : int
    created_at:datetime
    updated_at:datetime

    model_config = ConfigDict(from_attributes=True)

class CategoryUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
