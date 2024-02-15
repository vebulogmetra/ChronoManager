from fastapi import APIRouter
from src.services.users import UsersService
from src.schemas.users import UserSchemaIn, UserSchemaOut
from src.api.dependencies import UOWDep

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


users = []


@router.get("/users", response_model=list[UserSchemaOut])
async def get_users_handler(uow: UOWDep):
    users = await UsersService().get_users(uow=uow)
    return users


@router.post("/user")
async def create_user_handler(user_data: UserSchemaIn, uow: UOWDep):
    new_user_id = await UsersService().add_user(uow=uow, user=user_data)
    return new_user_id
