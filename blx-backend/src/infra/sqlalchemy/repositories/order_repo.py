from sqlalchemy.orm import Session
from typing import List

from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import mode
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class OrderRepositorie():

    def __init__(self, session: Session):
        self.session = session

    def save_order(self, order: schemas.Order):
        order_db = models.order(quantidade=order.quantidade,
                                  delivery_place=order.delivery_place,
                                  delivery_type=order.delivery_type,
                                  observation=order.observation,
                                  user_id=order.user_id,
                                  product_id=order.product_id
                                  )
        self.session.add(order_db)
        self.session.commit()
        self.session.refresh(order_db)

        return order_db

    def search_by_id(self, id: int) -> models.Order:
        query = select(models.Order).where(models.Order.id == id)
        order = self.session.execute(query).scalars().one()
        return order

    def list_orders_by_user_id(self, user_id: int):
        query = select(models.Order).where(
            models.Order.user_id == user_id)
        orders = self.session.execute(query).scalars().all()
        return orders

    def list_sales_by_user_id(self, user_id: int):
        query = select(models.Order) \
            .join_from(models.Order, models.Product) \
            .where(models.Product.user_id == user_id)
        orders = self.session.execute(query).scalars().all()
        return orders
