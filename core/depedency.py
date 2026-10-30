import jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from database.dependency import get_db
from core.security import decode_access_token
from models.users import Users


bearer_scheme = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token is invalid or expired",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        token = credentials.credentials

        payload = decode_access_token(token)

        email = payload.get("sub")

        if not email or not isinstance(email, str):
            raise credentials_exception

    except jwt.InvalidTokenError:
        raise credentials_exception

    user = db.query(Users).filter(
        Users.email == email
    ).first()

    if user is None:
        raise credentials_exception

    return user