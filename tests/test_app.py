import os

import pytest
import psycopg
from fastapi import status
from httpx import AsyncClient
from testcontainers.postgres import PostgresContainer

from garbage.dependencies import db_connect, create_engine
from garbage.repositories.v1.tables import users
from tests.fixtures import USER

USER_V1_PATH = "/api/v1/user"
postgres = PostgresContainer("postgres:16-alpine")


def get_connection():
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    username = os.getenv("DB_USERNAME", "postgres")
    password = os.getenv("DB_PASSWORD", "postgres")
    database = os.getenv("DB_NAME", "postgres")
    return psycopg.connect(f"host={host} dbname={database} user={username} password={password} port={port}")


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE users (
                    id serial PRIMARY KEY,
                    first_name varchar,
                    last_name varchar,
                    address varchar,
                    phone varchar,
                    email varchar,
                    is_active bool)
                """)
            conn.commit()


def delete_all_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users")
            conn.commit()


@pytest.fixture(scope="module", autouse=True)
def setup(request):
    container = postgres.start()

    # yield

    def remove_container(): #yield
        postgres.stop()

    request.addfinalizer(remove_container)
    os.environ["DB_CONN"] = postgres.get_connection_url()
    os.environ["DB_HOST"] = postgres.get_container_host_ip()
    os.environ["DB_PORT"] = postgres.get_exposed_port(5432)
    os.environ["DB_USERNAME"] = postgres.username
    os.environ["DB_PASSWORD"] = postgres.password
    os.environ["DB_NAME"] = postgres.dbname
    create_table()


@pytest.fixture(scope="function", autouse=True)
def setup_data():
    delete_all_users()


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
