from typing import Generic, TypeVar

from pydantic import BaseModel


T = TypeVar("T")


class ResponseSchema(BaseModel, Generic[T]):
    success: bool
    status_code: int
    message: str | None = None
    data: T | None = None