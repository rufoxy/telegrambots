from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
import os
from sqlalchemy import select
from sqlalchemy import ForeignKey, Table, Column, Integer

engine = create_async_engine(url=os.getenv('DB_URL'), echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id = mapped_column(BigInteger)


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(25))


class Status(Base):
    __tablename__ = 'statuses'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(25))


order_items = Table(
    'order_items',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id'), primary_key=True),
    Column('item_id', Integer, ForeignKey('Items.id'), primary_key=True),
    Column('quantity', Integer, default=1)  # Количество товара
)


class Item(Base):
    __tablename__ = 'Items'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(512))
    price: Mapped[int]
    image_url: Mapped[str] = mapped_column(String(255))

    # Связь с заказами через таблицу order_items
    orders = relationship("Order", secondary=order_items,
                          back_populates="items")


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    item: Mapped[int] = mapped_column(ForeignKey('Items.id'))
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))

    items = relationship("Item", secondary=order_items,
                         back_populates="orders")


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def init_statuses(async_session):
    async with async_session() as session:
        # Проверяем, есть ли уже записи в таблице statuses
        stmt = select(Status)
        result = await session.execute(stmt)
        if not result.scalars().all():  # Если таблица пустая
            # Добавляем начальные значения
            statuses = [
                Status(name="Новый заказ"),
                Status(name="В обработке"),
                Status(name="Завершён"),
                Status(name='В корзине')
            ]
            session.add_all(statuses)
            await session.commit()
