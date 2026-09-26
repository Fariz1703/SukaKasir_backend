from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import  Mapped, mapped_column,relationship
from datetime import datetime

from database.database import Base

class Supplier(Base):
    __tablename__ = "supplier"

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
    
    product_suppliers : Mapped[list["ProductSupplier"]]  = relationship(
        back_populates="supplier"
    )
    