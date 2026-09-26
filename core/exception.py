from typing import Any


class AppException(Exception):
    def __init__(
        self,
        status_code: int,
        message: str,
        data: Any = None,
    ):
        self.status_code = status_code
        self.message = message
        self.data = data

        super().__init__(message)