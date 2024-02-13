from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserSchemaBase(BaseModel):
    email: EmailStr


class UserSchemaIn(UserSchemaBase): ...


class UserSchemaOut(UserSchemaBase):
    id: int
    created_at: datetime
