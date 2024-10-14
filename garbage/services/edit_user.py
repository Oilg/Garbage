import re

from garbage.api.v1.types import UserModel, EditUserRequest
from garbage.errors import UserNotFoundError, UserInvalidNAmeError
from garbage.repositories.repository import UsersRepository


class EditUser:
    def __init__(self, users_database: UsersRepository):
        self.users_database: UsersRepository = users_database

    async def __call__(
            self,
            user_id: int,
            first_name: str,
            last_name: str,
            address: str,
            phone: str,
            email: str,
            is_active: bool
    ) -> UserModel:
        if not await self.users_database.user_exists_by_id(user_id):
            raise UserNotFoundError()
        LETTER_MATCH_PATTERN = re.compile(r"[a-яА-Яa-zA-Z\-]+$")
        if not LETTER_MATCH_PATTERN.match(first_name) or not LETTER_MATCH_PATTERN.match(last_name):
            raise UserInvalidNAmeError()
        return await self.users_database.update(
            EditUserRequest(
                id=user_id,
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone=phone,
                email=email,
                is_active=is_active,
            )
        )
