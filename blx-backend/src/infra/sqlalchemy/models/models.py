from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

# won't do it separate just to make it easier 
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    contact = Column(String)

    products = relationship('product', back_populates='user')
    orders = relationship('order', back_populates='user')


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    disponible = Column(Boolean)
    sizes = Column(String)
    user_id = Column(Integer, ForeignKey('user.id', name='fk_user'))

    user = relationship('user', back_populates='products')


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    delivery_location = Column(String)
    delivery_type = Column(String)
    observation = Column(String)

    user_id = Column(Integer, ForeignKey(
        'user.id', name='fk_order_user'))
    product_id = Column(Integer, ForeignKey(
        'product.id', name='fk_order_product'))

    user = relationship('user', back_populates='orders')
    product = relationship('product')
