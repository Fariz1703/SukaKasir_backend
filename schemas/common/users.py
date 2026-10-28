from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UsersBase(BaseModel):
    name : str
    password : str
    email :str
    role_id : int

class UsersCreate(UsersBase):
    pass

class UsersResponse(UsersBase):
    id : int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UsersUpdate(BaseModel):
    name : str | None = None
    password : str | None = None
    email :str | None = None
    role_id :int | None = None