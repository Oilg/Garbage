import pytest

from garbage.repositories.repository import UsersRepository
from tests.fixtures import USER


@pytest.fixture()
async def _enter_data_exclude_app_instance(user_repository: UsersRepository) -> None:
    for item in USER:
        await user_repository.create(item)
