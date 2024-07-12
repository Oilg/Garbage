from aiopg.sa import SAConnection
from sqlalchemy import Table

from garbage.api.v1.types import UserModel
from garbage.repositories.v1.tables import users


class BaseRepository:

    def __init__(self, connection: SAConnection) -> None:
        self._connection = connection


class UsersRepository(BaseRepository):

    table: Table = users

    async def user_exists_by_id(self, user_id: int) -> bool:
        get_query = self.table.select().where(self.table.c.phone == user_id)
        r_ = await self._connection.execute(get_query)
        result = await r_.fetchall()
        if len(result) == 1:
            return True
        return False

    async def user_exists_by_phone(self, phone: str) -> bool:
        get_query = self.table.select().where(self.table.c.phone == phone)
        r_ = await self._connection.execute(get_query)
        result = await r_.fetchall()
        if len(result) == 1:
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
