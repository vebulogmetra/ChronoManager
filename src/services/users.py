from src.schemas.users import UserSchemaIn
from src.utils.unitofwork import IUnitOfWork


class UsersService:
    async def add_user(self, uow: IUnitOfWork, user: UserSchemaIn):
        user_dict = user.model_dump()
        async with uow:
            user_id = await uow.users.add_one(user_dict)
            await uow.commit()
            return user_id

    async def get_users(self, uow: IUnitOfWork):
        async with uow:
            users = await uow.users.find_all()
            return users
