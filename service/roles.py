from sqlalchemy.orm import Session
from fastapi import status

from core.exception import AppException
from repository import roles as roles_repository 
from models.roles import Roles
from schemas.common.roles import RolesCreate, RolesUpdate


def create_role(
    db: Session,
    role_data: RolesCreate
) -> Roles:

    role = Roles(
        name= role_data.name,
        description=role_data.description
    )

    try:
        roles_repository.create(db, role)
        db.commit()
        db.refresh(role)
        return role
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to create role",
        ) from exc



def get_role(
    db: Session,
    role_id: int
) -> Roles | None:

    return roles_repository.get_role_by_id(db, role_id)

def get_roles(
    db: Session
) -> list[Roles]:

    return roles_repository.get_roles(db)


def update_role(
    db: Session,
    role_id: int,
    role_data: RolesUpdate
) -> Roles | None:

    role = get_role(db, role_id)

    if role is None:
        return None

    if role_data.name is not None:
        role.name = role_data.name

    if role_data.description is not None:
        role.description = role_data.description

    try:
        db.commit()
        db.refresh(role)
        return role
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to update role",
        ) from exc



def delete_role(
    db: Session,
    role_id: int
) -> Roles | None:

    role = get_role(db, role_id)

    if role is None:
        return None
    
    try:
        roles_repository.delete_role(db, role)
        db.commit()
        return role
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to delete role",
        ) from exc
