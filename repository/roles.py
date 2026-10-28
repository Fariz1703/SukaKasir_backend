from sqlalchemy.orm import Session

from models.roles import Roles

def create(db: Session, role: Roles) -> Roles:
    db.add(role)
    db.flush()
    return role

def get_role_by_id(
    db: Session,
    role_id: int
) -> Roles | None:
    return (
        db.query(Roles)
        .filter(Roles.id == role_id)
        .first()
    )

def get_roles(
    db: Session
) -> list[Roles]:
    return db.query(Roles).all()


def get_some_roles(
    db: Session,
    roles_ids: list[int]
) -> list[Roles]:
    return db.query(Roles).filter(Roles.id.in_(roles_ids)).all()

def delete_roles(
    db: Session,
    role: Roles,
) -> None:
    db.delete(role)
    db.flush()
