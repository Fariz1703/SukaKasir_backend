from fastapi import APIRouter, Depends, status
from core.exception import AppException
from sqlalchemy.orm import Session

from core.exception import AppException
from database.dependency import get_db
from schemas.common.respons import ResponseSchema
from schemas.common.roles import (
    RolesCreate,
    RolesResponse,
    RolesUpdate,
)
from service.roles import (
    create_role,
    get_role,
    get_roles,
    update_role,
    delete_role,
)


router = APIRouter(
    prefix="/api/role",
    tags=["Role Web"]
)


@router.post(
    "",
    response_model=ResponseSchema[RolesResponse],
    status_code=status.HTTP_201_CREATED
)
def create(
    Role_data: RolesCreate,
    db: Session = Depends(get_db)
):
    Role = create_role(db, Role_data)

    if Role is None:
        raise AppException(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Failed to create role"
        )
    
    return{
        "success" : True,
        "status_code": status.HTTP_201_CREATED,
        "message" : "Role created succesfully",
        "data" : Role
    }


@router.get(
    "",
    response_model=ResponseSchema[list[RolesResponse]]
)
def get_all(
    db: Session = Depends(get_db)
):
    Role = get_roles(db)

    if Role is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="role not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Role retrieved succesfully",
        "data" : Role
    }


@router.get(
    "/{role_id}",
    response_model=ResponseSchema[RolesResponse]
)
def get_one(
    role_id: int,
    db: Session = Depends(get_db)
):
    Role = get_role(db, role_id)

    if Role is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Role not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Role retrieved succesfully",
        "data" : Role
    }


@router.patch(
    "/{Role_id}",
    response_model=ResponseSchema[RolesResponse]
)
def update(
    Role_id: int,
    Role_data: RolesUpdate,
    db: Session = Depends(get_db)
):
    Role = update_role(
        db,
        Role_id,
        Role_data
    )

    if Role is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Role not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Role updated succesfully",
        "data" : Role
    }


@router.delete(
    "/{Role_id}",
    status_code=status.HTTP_200_OK,
    response_model=ResponseSchema[RolesResponse]
)
def delete(
    Role_id: int,
    db: Session = Depends(get_db)
):
    Role = delete_role(db, Role_id)

    if Role is None:
        raise AppException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="Role not found"
        )

    return{
        "success" : True,
        "status_code": status.HTTP_200_OK,
        "message" : "Role deleted succesfully",
        "data" : Role
    }