from aiopg.sa import SAConnection
from sqlalchemy import Table
from sqlalchemy.ext.asyncio import AsyncConnection

from garbage.api.v1.types import UserModel, CreateUserRequest
from garbage.repositories.v1.tables import users


class BaseRepository:

    def __init__(self, connection: AsyncConnection) -> None:
        self._connection = connection


class UsersRepository(BaseRepository):

    table: Table = users

    async def user_exists_by_id(self, user_id: int) -> bool:
        get_query = self.table.select().where(self.table.c.id == user_id)
        result = await self._connection.execute(get_query)
        if result.fetchone() is not None:
            return True
        else:
            return False

    async def user_exists_by_phone(self, phone: str) -> bool:
        get_query = self.table.select().where(self.table.c.phone == phone)
        result = await self._connection.execute(get_query)
        return result.fetchone() is not None

    async def create(self, user_input: CreateUserRequest) -> UserModel:
        insert_query = self.table.insert().values(user_input.dict()).returning(*self.table.c)
        result = await self._connection.execute(insert_query)
        user_row = result.fetchone()
        return UserModel(**user_row) if user_row else None

    async def delete(self, user_id: int):
        deactivate_query = self.table.update().where(self.table.c.id == user_id).values(is_active=False)
        await self._connection.execute(deactivate_query)

    async def get(self, user_id: int) -> UserModel | None:
        get_query = self.table.select().where(self.table.c.id == user_id)
        result = await self._connection.execute(get_query)
        user_row = result.fetchone()
        return UserModel(**user_row) if user_row is not None else None
