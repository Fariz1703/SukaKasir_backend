from fastapi import APIRouter, Depends, status
from core.exception import AppException
from sqlalchemy.orm import Session

from core.exception import AppException
from database.dependency import get_db
from schemas.common.respons import ResponseSchema
from schemas.common.users import (
    UsersCreate,
    UsersUpdate,
    UsersResponse,
)
from service.users import (
    create_user,
    get_user,
    get_users,
    update_user,
    delete_user,
)


router = APIRouter(
    prefix="/api/users",
    tags=["Users Web"]
)


@router.post(
    "",
    response_model=ResponseSchema[UsersResponse],
    status_code=status.HTTP_201_CREATED
)
def create(
    Users_data: UsersCreate,
    db: Session = Depends(get_db)
):
    Users = create_user(db, Users_data)

    if Users is None:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Failed to create User"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_201_CREATED,
        "message" : "User created succesfully",
        "data" : Users
    }


@router.get(
    "",
    response_model=ResponseSchema[list[UsersResponse]]
)
def get_all(
    db: Session = Depends(get_db)
):
    Users = get_users(db)

    if Users is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="User not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "User retrieved succesfully",
        "data" : Users
    }


@router.get(
    "/{Users_id}",
    response_model=ResponseSchema[UsersResponse]
)
def get_one(
    Users_id: int,
    db: Session = Depends(get_db)
):
    Users = get_user(db, Users_id)

    if Users is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="User not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "User retrieved succesfully",
        "data" : Users
    }


@router.patch(
    "/{Users_id}",
    response_model=ResponseSchema[UsersResponse]
)
def update(
    Users_id: int,
    Users_data: UsersUpdate,
    db: Session = Depends(get_db)
):
    Users = update_user(
        db,
        Users_id,
        Users_data
    )

    if Users is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="User not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "User updated succesfully",
        "data" : Users
    }


@router.delete(
    "/{Users_id}",
    status_code=status.HTTP_200_OK,
    response_model=ResponseSchema[UsersResponse]
)
def delete(
    Users_id: int,
    db: Session = Depends(get_db)
):
    Users = delete_user(db, Users_id)

    if Users is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="user not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "User deleted succesfully",
        "data" : Users
    }