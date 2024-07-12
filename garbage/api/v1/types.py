from pydantic import BaseModel, StrictStr, EmailStr


class UserModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: str
    phone: str
    email: str
    is_active: bool


class CreateUserRequest(BaseModel):
    first_name: StrictStr
    last_name: StrictStr
    address: StrictStr
    phone: StrictStr
    email: StrictStr


class CreateUserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: str
    phone: str
    email: str
    is_active: bool


class DeleteUserResponse(BaseModel):
    status_code: int


class GetUserResponse(BaseModel):
    status_code: int
    result: UserModel | None


