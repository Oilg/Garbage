class BaseError(Exception):
    message = "Unexpected exception"

    @property
    def code(
        self,
    ) -> str:
        return self.message.lower().replace(" ", "_")

    def __repr__(self) -> str:
        """Для отображения полного контекста ошибки в stderr"""
        context = [f"{key}: {value!r}" for key, value in self.__dict__.items()]
        context_repr = "\n".join(context)

        return f"{self.message}\n{context_repr}"

    __str__ = __repr__

    def __init__(self) -> None:
        super().__init__(self.message)


class NotFoundError(BaseError):
    status_code = 404
    message = "Not Found"


class UserNotFoundError(NotFoundError):
    message = "User Not Found"


class UserWithPhoneExistError(BaseError):
    status_code = 409

    def __init__(self, phone: str) -> None:
        self.message = f"User with same phone number {phone} already exists"
        super().__init__()


class UserInvalidNAmeError(BaseError):
    status_code = 422
    message = f"First name and Last name should contains only letters"
