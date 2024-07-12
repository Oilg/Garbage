from fastapi import status
from fastapi.responses import ORJSONResponse


async def request_exception_handler() -> ORJSONResponse:
    return ORJSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": "Something went wrong"})


async def request_not_found_handler() -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": "User not found in garbage service"},
    )
