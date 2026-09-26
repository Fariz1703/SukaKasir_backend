from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from database.database import Base


class TransactionType(Base):
    __tablename__ = "transaction_type"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name : Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    description : Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    need_supplier : Mapped[bool] = mapped_column(
        nullable=False,
        default=False
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

    transactions: Mapped[list["Transaction"]] = relationship(
        back_populates="transaction_type"
    )