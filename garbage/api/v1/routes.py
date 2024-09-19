from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from starlette import status

from garbage.api.v1.types import CreateUserResponse, CreateUserRequest, DeleteUserResponse, GetUserResponse
from garbage.dependencies import get_create_user_service, get_delete_user_service, get_user_service
from garbage.services.create_user import CreateUser
from garbage.services.delete_user import DeleteUser
from garbage.services.get_user import GetUser

api_router_user = APIRouter(default_response_class=ORJSONResponse)


@api_router_user.post(path="", response_model=CreateUserResponse)
async def create_user(
        data: CreateUserRequest,
        create_user_service: CreateUser = Depends(get_create_user_service),
) -> CreateUserResponse:
    user = await create_user_service(data.first_name, data.last_name, data.address, data.phone, data.email)
    return CreateUserResponse(status_code=status.HTTP_200_OK, result=user)


@api_router_user.delete(path="/{id}", response_model=DeleteUserResponse)
async def delete_user(
        user_id: int,
        delete_user_service: DeleteUser = Depends(get_delete_user_service),
) -> DeleteUserResponse:
    await delete_user_service(user_id=user_id)
    return DeleteUserResponse(status_code=status.HTTP_200_OK, result=f"User with id {user_id} was deleted successfully")


@api_router_user.get(path="/{id}", response_model=GetUserResponse)
async def get_user(
        id: int,
        get_users_service: GetUser = Depends(get_user_service)
) -> GetUserResponse:
    user = await get_users_service(user_id=id)
    return GetUserResponse(result=user)
