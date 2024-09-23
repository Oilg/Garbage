import re

from starlette import status
from starlette.exceptions import HTTPException

from garbage.api.v1.types import UserModel, EditUserRequest
from garbage.errors import invalid_name, user_id_doesnt_exist
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
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=user_id_doesnt_exist)
        LETTER_MATCH_PATTERN = re.compile(r"[a-яА-Яa-zA-Z\-]+$")
        if not LETTER_MATCH_PATTERN.match(first_name) or not LETTER_MATCH_PATTERN.match(last_name):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=invalid_name
            )
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
