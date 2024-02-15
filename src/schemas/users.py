from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserSchemaBase(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True


class UserSchemaIn(UserSchemaBase): ...


class UserSchemaOut(UserSchemaBase):
    id: int
    created_at: datetime


class UserSchemaUpdate(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True
