from sqlalchemy import ForeignKey, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from database.database import Base



class Transaction(Base):
    __tablename__ = "transaction"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    transaction_type_id : Mapped[int] = mapped_column(
       ForeignKey("transaction_type.id")
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

    transaction_type : Mapped["TransactionType"] = relationship(
        back_populates = "transactions"
    )

    transaction_item : Mapped[list["TransactionItem"]] = relationship(
        back_populates = "transactions"
    )