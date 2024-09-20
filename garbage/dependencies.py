from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncConnection

from garbage.repositories.repository import UsersRepository
from garbage.services.create_user import CreateUser
from garbage.services.delete_user import DeleteUser
from garbage.services.get_user import GetUserService


async def create_engine() -> AsyncEngine:
    return create_async_engine(
        "postgresql+asyncpg://admin:root@localhost:5432/postgres"
    )


async def db_connect(engine: AsyncConnection = Depends(create_engine)):
    async with engine.begin() as conn:
        yield conn


async def user_repository(conn: AsyncConnection = Depends(db_connect)) -> UsersRepository:
    return UsersRepository(conn)


async def get_create_user_service(users_db: UsersRepository = Depends(user_repository)) -> CreateUser:
    return CreateUser(users_database=users_db)


async def get_delete_user_service(users_db: UsersRepository = Depends(user_repository)) -> DeleteUser:
    return DeleteUser(users_database=users_db)


async def get_user_service(users_db: UsersRepository = Depends(user_repository)) -> GetUserService:
    return GetUserService(users_database=users_db)
