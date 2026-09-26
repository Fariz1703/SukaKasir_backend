from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import  Mapped, mapped_column,relationship
from datetime import datetime

from database.database import Base

class Unit(Base):
    __tablename__ = "unit"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name : Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    description : Mapped[str] = mapped_column(
        String(255),
        nullable=False
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
    
    products : Mapped[list["Product"]]  = relationship(
        back_populates="unit"
    )
    