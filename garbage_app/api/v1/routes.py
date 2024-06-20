from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from starlette import status

from garbage_app.api.v1.types import CreateUserResponse, CreateUserRequest, DeleteUserResponse
from garbage_app.services.create_user import CreateUser
from garbage_app.services.delete_user import DeleteUser

api_router_user = APIRouter(default_response_class=ORJSONResponse)


@api_router_user.post(path="", response_model=CreateUserResponse)
async def create_user(
        data: CreateUserRequest,
        create_user_service: CreateUser = Depends(),
) -> CreateUserResponse:
    await create_user_service(data.first_name, data.last_name, data.address, data.phone, data.email)
    return CreateUserResponse(status_code=status.HTTP_200_OK)


@api_router_user.delete(path="/{id}", response_model=DeleteUserResponse)
async def delete_user(
        user_id: int,
        delete_user_service: DeleteUser = Depends(),
) -> DeleteUserResponse:
    await delete_user_service(user_id=user_id)
    return DeleteUserResponse(status_code=status.HTTP_200_OK)
