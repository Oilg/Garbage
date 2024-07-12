from starlette import status
from starlette.exceptions import HTTPException

from garbage.api.v1.types import UserModel
from garbage.errors import user_with_phone_exists_error
from garbage.repositories.repository import UsersRepository


class CreateUser:
    def __init__(self, users_database: UsersRepository):
        self.users_database: UsersRepository = users_database

    async def __call__(self, first_name: str, last_name: str, address: str, phone: str, email: str) -> None:
        if await self.users_database.user_exists_by_phone(phone):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail=user_with_phone_exists_error)
        await self.users_database.create(
            UserModel(
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone=phone,
                email=email,
            )
        )
        return