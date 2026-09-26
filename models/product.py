from sqlalchemy import ForeignKey ,String , DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from database.database import Base



class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    sku : Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    category_id : Mapped[int] = mapped_column(
        ForeignKey("category.id")
    )

    name : Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    unit_id : Mapped[int] = mapped_column(
        ForeignKey("unit.id")
    )

    unit_size : Mapped[int] = mapped_column(
        nullable= False
    )

    sell_price : Mapped[int] = mapped_column(
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

    unit : Mapped["Unit"]  = relationship(
        back_populates="products"
    )

    category : Mapped["Category"]  = relationship(
        back_populates="products"
    )

    transaction_items : Mapped[list["TransactionItem"]] = relationship(
        back_populates="product"
    )

    product_suppliers : Mapped[list["ProductSupplier"]]  = relationship(
        back_populates="product"
    )