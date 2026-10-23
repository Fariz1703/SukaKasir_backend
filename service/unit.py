from sqlalchemy.orm import Session
from fastapi import status

from core.exception import AppException
from repository import unit as unit_repository 
from models.unit import Unit
from schemas.common.unit import UnitCreate, UnitUpdate


def create_unit(
    db: Session,
    unit_data: UnitCreate
) -> Unit:

    unit = Unit(
        name=unit_data.name,
        description=unit_data.description
    )

    try:
        unit_repository.create(db, unit)
        db.commit()
        db.refresh(unit)
        return unit
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to create unit",
        ) from exc



def get_unit(
    db: Session,
    unit_id: int
) -> Unit | None:

    return unit_repository.get_unit_by_id(db, unit_id)

def get_units(
    db: Session
) -> list[Unit]:

    return unit_repository.get_units(db)


def update_unit(
    db: Session,
    unit_id: int,
    unit_data: UnitUpdate
) -> Unit | None:

    unit = get_unit(db, unit_id)

    if unit is None:
        return None

    if unit_data.name is not None:
        unit.name = unit_data.name

    if unit_data.description is not None:
        unit.description = unit_data.description

    try:
        db.commit()
        db.refresh(unit)
        return unit
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to update unit",
        ) from exc



def delete_unit(
    db: Session,
    unit_id: int
) -> Unit | None:

    unit = get_unit(db, unit_id)

    if unit is None:
        return None
    
    try:
        unit_repository.delete_unit(db, unit)
        db.commit()
        return unit
    except Exception as exc:
        db.rollback()
        raise AppException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to delete unit",
        ) from exc
