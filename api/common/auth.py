from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.exception import AppException
from database.dependency import get_db
from service.auth import login_user
from schemas.common.auth import LoginRequest, TokenResponse


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    token = login_user(
        db,
        data.email,
        data.password
    )

    if not token:
        raise AppException(
            status_code=401,
            message="email or password is incorrect"
        )

    return TokenResponse(
        access_token=token,
        token_type="bearer"
    )