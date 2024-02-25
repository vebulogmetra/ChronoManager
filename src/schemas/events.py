from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventSchemaBase(BaseModel):
    title: str
    description: str
    owner_id: Optional[int] = None
    expired_at: datetime
    notify_at: datetime

    class Config:
        from_attributes = True
        json_encoders = {datetime: lambda dt: dt.strftime("%Y-%m-%d %H:%M:%S")}


class EventSchemaCreateResponse(BaseModel):
    event_id: int


class EventSchemaIn(EventSchemaBase): ...


class EventSchemaOut(EventSchemaBase):
    id: int
    created_at: datetime


class EventSchemaUpdate(BaseModel):
    title: str
    description: str
    expired_at: str
    notify_at: str

    class Config:
        from_attributes = True
