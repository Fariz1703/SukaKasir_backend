from pydantic import BaseModel, ConfigDict
from datetime import datetime

class RolesBase(BaseModel):
    name : str
    description : str

class RolesCreate(RolesBase):
    pass

class RolesResponse(RolesBase):
    id : int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class RolesUpdate(BaseModel):
    name : str | None = None
    description : str | None = None