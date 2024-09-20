from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from starlette.exceptions import HTTPException


async def request_exception_handler(request: Request, exc: RequestValidationError) -> ORJSONResponse:
    return ORJSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": "Something went wrong"})


async def request_not_found_handler(request: Request, exc: HTTPException) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": "User not found in garbage service"},
    )
