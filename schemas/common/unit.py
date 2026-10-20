from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UnitBase(BaseModel):
    name : str
    description : str

class UnitCreate(UnitBase):
    pass

class UnitResponse(UnitBase):
    id : int
    created_at:datetime
    updated_at:datetime

    model_config = ConfigDict(from_attributes=True)

class UnitUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
