from fastapi import APIRouter
from src.repositories.users import UsersRepository
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
    users = await UsersRepository.find_all()
    return users


@router.post("/user", response_model=list[UserSchemaOut])
async def create_user_handler(user_data: UserSchemaIn):
    new_user = await UsersRepository().add_one(data=user_data.model_dump())
    return new_user
