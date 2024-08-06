import pytest

from garbage.repositories.repository import UsersRepository
from tests.fixtures import USER


# инициализация и старт контейнера
# подключение к контейнеру и создание, тушение таблиц
#    фикстуры на наполнение данных
# тестовый репозиторий с подключением из предыдущей фикстуры
# тестовый сервис с тестовым репозиторием



@pytest.fixture()
async def _enter_data_user(user_repository: UsersRepository) -> None:
    for item in USER:
        await user_repository.create(item)
