from sqlalchemy.orm import Session

from models.unit import Unit
from schemas.unit import UnitCreate, UnitUpdate


def create_unit(
    db: Session,
    unit_data: UnitCreate
) -> Unit:

    unit = Unit(
        name=unit_data.name,
        description=unit_data.description
    )

    db.add(unit)
    db.commit()
    db.refresh(unit)

    return unit


def get_unit(
    db: Session,
    unit_id: int
) -> Unit | None:

    return (
        db.query(Unit)
        .filter(Unit.id == unit_id)
        .first()
    )


def get_units(
    db: Session
) -> list[Unit]:

    return db.query(Unit).all()


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

    db.commit()
    db.refresh(unit)

    return unit


def delete_unit(
    db: Session,
    unit_id: int
) -> Unit | None:

    unit = get_unit(db, unit_id)

    if unit is None:
        return None

    db.delete(unit)
    db.commit()

    return unit