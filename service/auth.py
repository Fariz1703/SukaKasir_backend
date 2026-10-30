from sqlalchemy.orm import Session

from core.exception import AppException
from repository.users import  get_user_by_email
from core.security import (
    verify_password,
    create_access_token
)


def login_user(
    db: Session,
    email: str,
    password: str
):
    
    user = get_user_by_email(db, email)

    if not user:
        raise AppException(
            status_code=401,
            message="email or password is incorrect"
            )

    if not verify_password(
        password,
        user.password
    ):
        raise AppException(
            status_code=401,
            message="email or password is incorrect"
        )

    token = create_access_token({
        "sub": user.email
    })

    return token