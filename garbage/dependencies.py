from aiopg.sa import SAConnection
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from garbage.repositories.repository import UsersRepository
from garbage.services.create_user import CreateUser
from garbage.services.delete_user import DeleteUser


async def create_engine() -> AsyncEngine:
    return create_async_engine(
        "postgresql+asyncpg://user:password@localhost/db"
    )


async def db_connect(engine: AsyncEngine = Depends(create_engine)):
    async with engine.connect() as conn:
        yield conn
        await conn.close()


async def user_repository(conn: SAConnection = Depends(db_connect)) -> UsersRepository:
    return UsersRepository(conn)


async def get_create_user_service(users_db: UsersRepository = Depends(user_repository)) -> CreateUser:
    return CreateUser(users_database=users_db)


async def get_delete_user_service(users_db: UsersRepository = Depends(user_repository)) -> DeleteUser:
    return DeleteUser(users_database=users_db)
