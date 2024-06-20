from typing import cast
from fastapi import Request


class Main:
    def __init__(self) -> None:
        pass

    def __call__(self) -> None:
        pass


async def get_main(request: Request) -> Main:
    return cast(Main, request.app.state.main)
