from src.routers.auth_utils import get_logged_user
from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.user_repo import UserRepositorie 
from src.schemas.schemas import Order, User

router = APIRouter()


@router.post('/orders',
             status_code=status.HTTP_201_CREATED,
             response_model=Order)
def make_order(order: Order, session: Session = Depends(get_db)):
    created_order = UserRepositorie(session).save_order(order)
    return created_order


@router.get('/orders/{id}', response_model=Order)
def show_order(id: int, session: Session = Depends(get_db)):
    try:
        order = UserRepositorie(session).get_by_id(id)
        return order
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There's no order with such id={id}")


@router.get('/orders', response_model=List[Order])
def list_orders(user: User = Depends(get_logged_user),
                   session: Session = Depends(get_db)):
    orders = UserRepositorie(
        session).list_my_orders_by_id(user.id)
    return orders


@router.get('/orders/{user_id}/sales', response_model=List[Order])
def list_sales(user_id: int, session: Session = Depends(get_db)):
    orders = UserRepositorie(
        session).list_my_sales_by_user_id(user_id)
    return orders
