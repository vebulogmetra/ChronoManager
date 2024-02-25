from pydantic import BaseModel, EmailStr, root_validator, Field
from datetime import datetime
from typing import Optional


class UserSchemaBase(BaseModel):
    email: Optional[EmailStr] = Field(default=None)
    tg_user_id: Optional[int] = Field(default=None, ge=0)

    class Config:
        from_attributes = True
        validate_assignment = True

    @root_validator(pre=True)
    def validate_xor(cls, values):
        if sum([bool(v) for v in values.values()]) != 1:
            raise ValueError("Either email or tg_user_id must be set.")
        return values


class UserSchemaIn(UserSchemaBase): ...


class UserSchemaOut(UserSchemaBase):
    id: int
    access_token: str
    created_at: datetime


class UserSchemaUpdate(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True


class UserCreds(BaseModel):
    login: str
    password: str


class UserToken(BaseModel):
    token: str
