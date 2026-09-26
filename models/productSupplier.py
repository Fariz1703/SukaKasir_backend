from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


from database.database import Base

class ProductSupplier(Base):
    __tablename__ = "product_supplier"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    product_id : Mapped[int] = mapped_column(
        ForeignKey("product.id")
    )

    supplier_id : Mapped[int] = mapped_column(
        ForeignKey("supplier.id"),
    )

    buy_price : Mapped[int] = mapped_column(
        nullable= False
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

    supplier : Mapped["Supplier"]  = relationship(
        back_populates="product_suppliers"
    )

    product : Mapped["Product"]  = relationship(
        back_populates="product_suppliers"
    )

    transaction_items : Mapped[list["TransactionItem"]] = relationship(
        back_populates="product_supplier"
    )
