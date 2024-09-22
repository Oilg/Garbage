from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from starlette import status

from garbage.api.v1.types import CreateUserResponse, CreateUserRequest, DeleteUserResponse, EditUserResponse, \
    EditUserRequest
from garbage.dependencies import get_create_user_service, get_delete_user_service, get_edit_user_service
from garbage.services.create_user import CreateUser
from garbage.services.delete_user import DeleteUser
from garbage.services.edit_user import EditUser

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
        id: int,
        delete_user_service: DeleteUser = Depends(get_delete_user_service),
) -> DeleteUserResponse:
    await delete_user_service(user_id=id)
    return DeleteUserResponse(status_code=status.HTTP_200_OK, result=f"User with id {id} was deleted successfully")


@api_router_user.patch(path="", response_model=EditUserResponse)
async def edit_user(
        data: EditUserRequest,
        edit_user_service: EditUser = Depends(get_edit_user_service),
) -> EditUserResponse:
    user = await edit_user_service(
        data.id,
        data.first_name,
        data.last_name,
        data.address,
        data.phone,
        data.email,
        data.is_active
    )
    return EditUserResponse(status_code=status.HTTP_200_OK, result=user)
