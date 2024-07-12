from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError

from garbage.api.v1.handlers import request_exception_handler, request_not_found_handler
from garbage.api.v1.routes import api_router_user as api_router_user_v1
from garbage.settings import Settings

SERVICE_NAME = "garbage"


def create_app() -> FastAPI:
    app = FastAPI(title=SERVICE_NAME)

    app.include_router(api_router_user_v1, prefix="/api/v1/user")
    app.add_exception_handler(RequestValidationError, request_exception_handler)
    app.add_exception_handler(status.HTTP_404_NOT_FOUND, request_not_found_handler)

    return app


if __name__ == "__main__":
    settings_ = Settings
    app_ = create_app()
