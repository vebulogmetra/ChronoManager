from fastapi import APIRouter
from src.schemas.users import UserSchemaIn, UserSchemaOut
from random import randint
from datetime import datetime

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


users = []


@router.get("/users", response_model=list[UserSchemaOut])
async def get_users_handler():
    return users


@router.post("/user", response_model=list[UserSchemaOut])
async def create_user_handler(event_data: UserSchemaIn):
    users.append(
        UserSchemaOut(
            id=randint(1, 10), email="example@example.com", created_at=datetime.now()
        )
    )
    return users
