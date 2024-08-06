from starlette import status
from starlette.exceptions import HTTPException

from garbage.repositories.repository import UsersRepository


class DeleteUser:
    def __init__(self, users_database: UsersRepository):
        self.users_database: UsersRepository = users_database

    async def __call__(self, user_id: int) -> str:
        if not await self.users_database.user_exists_by_id(user_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        await self.users_database.delete(user_id)
        return f"{user_id} was deleted"
