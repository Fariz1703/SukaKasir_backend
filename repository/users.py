from sqlalchemy.orm import Session

from models.users import Users

def create(db: Session, user: Users) -> Users:
    db.add(user)
    db.flush()
    return user

def get_user_by_id(
    db: Session,
    user_id: int
) -> Users | None:
    return (
        db.query(Users)
        .filter(Users.id == user_id)
        .first()
    )

def get_users(
    db: Session
) -> list[Users]:
    return db.query(Users).all()


def get_some_users(
    db: Session,
    user_ids: list[int]
) -> list[Users]:
    return db.query(Users).filter(Users.id.in_(user_ids)).all()

def delete_user(
    db: Session,
    User: Users,
) -> None:
    db.delete(User)
    db.flush()
