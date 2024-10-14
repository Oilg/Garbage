from garbage.errors import UserNotFoundError
from garbage.repositories.repository import UsersRepository


class DeleteUser:
    def __init__(self, users_database: UsersRepository):
        self.users_database: UsersRepository = users_database

    async def __call__(self, user_id: int) -> str:
        if not await self.users_database.user_exists_by_id(user_id):
            raise UserNotFoundError()
        await self.users_database.delete(user_id)
        return f"{user_id} was deleted"
