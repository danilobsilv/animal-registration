from pydantic import BaseModel
from typing import Optional, List


class SimpleProduct(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    disponible: bool

    class Config:
        orm_mode = True


class User(BaseModel):
    id: Optional[int] = None
    name: str
    contact: str
    password: str
    products: List[SimpleProduct] = []

    class Config:
        orm_mode = True


class SimpleUser(BaseModel):
    id: Optional[int] = None
    name: str
    contact: str

    class Config:
        orm_mode = True


class LoginData(BaseModel):
    password: str
    contact: str


class LoginSucess(BaseModel):
    user: SimpleUser
    access_token: str


class Product(BaseModel):
    id: Optional[int] = None
    name: str
    details: str
    price: float
    disponible: bool = False
    user_id: Optional[int]
    user: Optional[SimpleUser]

    class Config:
        orm_mode = True


class Order(BaseModel):
    id: Optional[int] = None
    amount: int
    place_delivery: Optional[str]
    type_delivery: str
    observation: Optional[str] = 'No observations'

    user_id: Optional[int]
    product_id: Optional[int]

    user: Optional[SimpleUser]
    product: Optional[SimpleProduct]

    class Config:
        orm_mode = True
