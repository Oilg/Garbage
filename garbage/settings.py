from pydantic import BaseSettings, PositiveInt
from pydantic.networks import PostgresDsn


class Settings(BaseSettings):
    postgres_dsn: PostgresDsn
    pg_pool_size: PositiveInt = 10
    pg_log_queries: bool = False
    pg_connection_timeout: PositiveInt = 60

    class Config:
        env_file = "local.env"
