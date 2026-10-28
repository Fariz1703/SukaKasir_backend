from sqlalchemy import String, DateTime, ForeignKey, func
from sqlalchemy.orm import  Mapped, mapped_column,relationship
from datetime import datetime

from database.database import Base

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name : Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    email : Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    password : Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    role_id : Mapped[int] = mapped_column(
        ForeignKey("roles.id")
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )
    
    roles : Mapped["Roles"]  = relationship(
        back_populates="users"
    )
    