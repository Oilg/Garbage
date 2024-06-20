from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from aiopg.sa import SAConnection
from sqlalchemy import Table

from garbage_app.api.v1.types import UserModel
from garbage_app.repositories.v1.tables import users


class UsersRepository:

    table: Table = users

    def __init__(self, connection: SAConnection) -> None:
        self._connection = connection

    @asynccontextmanager
    async def transaction(self) -> AsyncGenerator[None, None]:
        async with self._connection.begin():
            yield

    async def user_exists_by_id(self, user_id: int) -> bool:
        async with self._connection.execute(
            self.table.select().where(self.table.c.phone == user_id)
        ) as raws:
            if raws.rawcount == 1:
                return True
            return False

    async def user_exists_by_phone(self, phone: str) -> bool:
        async with self._connection.execute(
            self.table.select().where(self.table.c.phone == phone)
        ) as raws:
            if raws.rawcount == 1:
                return True
            return False

    async def create(self, user_input: UserModel) -> UserModel:
        insert_query = self.table.insert().values(user_input.dict()).returning(*self.table.c)
        r_ = await self._connection.execute(insert_query)
        result = await r_.fetchone()
        return UserModel(**dict(result))

    async def delete(self, user_id: int) -> UserModel:
        deactivate_query = self.table.update().where(self.table.c.id == user_id).values(is_active=False)
        r_ = await self._connection.execute(deactivate_query)
        result = await r_.fetchone()
        return UserModel(**dict(result))
