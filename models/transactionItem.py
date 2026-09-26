from sqlalchemy import ForeignKey, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from database.database import Base



class TransactionItem(Base):
    __tablename__ = "transaction_item"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    product_id : Mapped[int] = mapped_column(
        ForeignKey("product.id")
    )

    product_supplier_id : Mapped[int] = mapped_column(
        ForeignKey("product_supplier.id"),
        nullable=True
    )

    transaction_id : Mapped[int] = mapped_column(
        ForeignKey("transaction.id")
    )

    quantity : Mapped[int] = mapped_column(
    )

    unit_price : Mapped[int] = mapped_column(
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

    transactions : Mapped["Transaction"] = relationship(
        back_populates = "transaction_item"
    )

    product : Mapped["Product"] = relationship(
        back_populates = "transaction_items"
    )

    product_supplier : Mapped["ProductSupplier"] = relationship(
        back_populates = "transaction_items"
    )