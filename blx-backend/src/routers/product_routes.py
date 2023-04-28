from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Product, SimpleProduct
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.product_repo import ProductRepositorie

router = APIRouter()


@router.post('/products',
             status_code=status.HTTP_201_CREATED,
             response_model=SimpleProduct)
def create_product(
        product: Product,
        session: Session = Depends(get_db)):
    created_product = ProductRepositorie(session).create(product)
    return created_product


@router.get('/products', response_model=List[SimpleProduct])
def list_products(session: Session = Depends(get_db)):
    products = ProductRepositorie(session).list()
    return products


@router.get('/products/{id}')
def show_product(id: int, session: Session = Depends(get_db)):
    product_found = ProductRepositorie(session).buscarPorId(id)
    if not product_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"There's no product with such id={id}")
    return product_found


@router.put('/products/{id}', response_model=SimpleProduct)
def update_product(
        id: int,
        product: Product,
        session: Session = Depends(get_db)):
    ProductRepositorie(session).editar(id, product)
    product.id = id
    return product


@router.delete('/products/{id}')
def delete_product(id: int, session: Session = Depends(get_db)):
    ProductRepositorie(session).delete(id)
    return
