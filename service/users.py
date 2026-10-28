
from sqlalchemy.orm import Session
from fastapi import status
from sqlalchemy import select

from core.exception import AppException
from core.pwSecurity import hash_password
from repository import users as user_repository
from models.users import Users
from schemas.common.users import UsersCreate, UsersUpdate



def create_user(
    db: Session,
    user_data: UsersCreate,
) -> Users:
    email = user_data.email.strip().lower()

    existing_user = db.scalar(
        select(Users.id).where(Users.email == email)
    )

    if existing_user is not None:
        raise AppException(
            status_code=409,
            message="Email already exists",
        )

    hashed_pw = hash_password(user_data.password)

    user = Users(
        name=user_data.name,
        email=email,
        password=hashed_pw,
        role_id=user_data.role_id,
    )

    try:
        user_repository.create(db, user)
        db.commit()
        db.refresh(user)
        return user

    except AppException:
        db.rollback()
        raise

    except Exception as exc:
        db.rollback()
        logger.exception("Failed to create user")

        raise AppException(
            status_code=500,
            message="Failed to create user",
        ) from exc


def get_user(
    db: Session,
    user_id: int,
) -> Users | None:
    return user_repository.get_user_by_id(db, user_id)


def get_users(
    db: Session,
) -> list[Users]:
    return user_repository.get_users(db)


def update_user(
    db: Session,
    user_id: int,
    user_data: UsersUpdate,
) -> Users | None:
    user = get_user(db, user_id)

    if user is None:
        return None

    if user_data.name is not None:
        user.name = user_data.name

    if user_data.email is not None:
        user.email = user_data.email

    if user_data.password is not None:
        user.password = hash_password(user_data.password)

    if user_data.role_id is not None:
        user.role = user_data.role_id

    try:
        db.commit()
        db.refresh(user)
        return user
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to update user",
        ) from exc


def delete_user(
    db: Session,
    user_id: int,
) -> Users | None:
    user = get_user(db, user_id)

    if user is None:
        return None

    try:
        user_repository.delete_user(db, user)
        db.commit()
        return user
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to delete user",
        ) from exc
