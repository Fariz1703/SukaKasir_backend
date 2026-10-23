from sqlalchemy.orm import Session

from models.unit import Unit

def create(db: Session, unit: Unit) -> Unit:
    db.add(unit)
    db.flush()
    return unit

def get_unit_by_id(
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

def get_some_units(
    db: Session,
    unit_ids: list[int]
) -> list[Unit]:
    return db.query(Unit).filter(Unit.id.in_(unit_ids)).all()

def delete_unit(
    db: Session,
    unit: Unit,
) -> None:
    db.delete(unit)
    db.flush()
