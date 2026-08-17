from typing import Generic, TypeVar, Sequence
from pydantic import BaseModel, Field

T = TypeVar("T")

class Page(BaseModel, Generic[T]):
    items: Sequence[T]
    total: int
    skip: int = Field(default=0, ge=0)
    limit: int = Field(default=20, gt=0, le=100)

class PaginationParams(BaseModel):
    skip: int = Field(default=0, ge=0)
    limit: int = Field(default=20, gt=0, le=100)
