from starlette import status
from starlette.exceptions import HTTPException

from garbage.api.v1.types import UserModel
from garbage.repositories.repository import UsersRepository


class GetUserService:
    def __init__(self, users_database: UsersRepository):
        self.users_database: UsersRepository = users_database

    async def __call__(self, user_id: int) -> UserModel:
        user_result = await self.users_database.get(user_id)
        if user_result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user_result
