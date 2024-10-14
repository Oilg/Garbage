from typing import Optional

from pydantic import BaseModel, StrictStr, EmailStr, conint, StrictBool, constr


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
    email: EmailStr


class CreateUserResponse(BaseModel):
    result: UserModel | None


class DeleteUserResponse(BaseModel):
    status_code: int


class GetUserResponse(BaseModel):
    result: UserModel | None


class EditUserRequest(BaseModel):
    id: conint(ge=1, le=2147483647)
    first_name: StrictStr
    last_name: StrictStr
    address: StrictStr
    phone: Optional[
        constr(
            strip_whitespace=True,
            regex=r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$",
        )
    ]
    email: EmailStr
    is_active: StrictBool


class EditUserResponse(BaseModel):
    result: UserModel | None

