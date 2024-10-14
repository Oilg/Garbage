import re

from garbage.api.v1.types import CreateUserRequest, UserModel
from garbage.errors import UserWithPhoneExistError, UserInvalidNAmeError
from garbage.repositories.repository import UsersRepository


class CreateUser:
    def __init__(self, users_database: UsersRepository):
        self.users_database: UsersRepository = users_database

    async def __call__(self, first_name: str, last_name: str, address: str, phone: str, email: str) -> UserModel:
        LETTER_MATCH_PATTERN = re.compile(r"[a-яА-Яa-zA-Z\-]+$")
        if not LETTER_MATCH_PATTERN.match(first_name) or not LETTER_MATCH_PATTERN.match(last_name):
            raise UserInvalidNAmeError()
        if await self.users_database.user_exists_by_phone(phone):
            raise UserWithPhoneExistError()
        return await self.users_database.create(
            CreateUserRequest(
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone=phone,
                email=email,
            )
        )

