from pydantic import PositiveInt
from pydantic.networks import PostgresDsn


class Settings:
    postgres_dsn: PostgresDsn
    microservice_postgres_dsn: PostgresDsn
    pg_pool_size: PositiveInt = 10
    pg_log_queries: bool = False
    pg_connection_timeout: PositiveInt = 60
