from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventSchemaBase(BaseModel):
    title: str
    description: str
    owner_id: Optional[int] = None
    expired_at: str

    class Config:
        from_attributes = True


class EventSchemaIn(EventSchemaBase): ...


class EventSchemaOut(EventSchemaBase):
    id: int
    created_at: datetime


class EventSchemaUpdate(BaseModel):
    title: str
    description: str
    expired_at: str

    class Config:
        from_attributes = True
