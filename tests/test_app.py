import pytest
from fastapi import status
from httpx import AsyncClient

from tests.fixtures import USER

USER_V1_PATH = "/api/v1/user"


@pytest.mark.asyncio()
@pytest.mark.parametrize(
    ("first_name", "last_name", "address", "phone", "email", "result"),
    [
        ("Mega", "Azazaev", "Moscwe", "777", "azazaev@mail.ru", status.HTTP_200_OK),
        # (4, status.HTTP_400_BAD_REQUEST),
    ],
)
async def test_create_user(test_client: AsyncClient, first_name, last_name, address, phone, email, result):
    response = await test_client.post(
        f"{USER_V1_PATH}",
        json={"first_name": first_name, "last_name": last_name, "address": address, "phone": phone, "email": email}
    )
    assert response.status_code == result
    assert response.json() == {""}


@pytest.mark.asyncio()
@pytest.mark.usefixtures("_enter_data_exclude_app_instance")
async def test_create_user_already_exists_with_same_phone(test_client: AsyncClient):
    response = await test_client.post(
        f"{USER_V1_PATH}",
        json=USER.copy()
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {"detail": "already exist"}
