from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
# from sqlalchemy.sql.expression import select
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class ProductRepositorie():

    def __init__(self, db: Session):
        self.session = db

    def create(self, product: schemas.Product):
        db_product = models.Product(nome=product.nome,
                                    detail=product.detail,
                                    price=product.price,
                                    disponible=product.disponible,
                                    user_id=product.user_id)
        self.session.add(db_product)
        self.session.commit()
        self.session.refresh(db_product)
        return db_product

    def listProd(self):
        products = self.session.query(models.Product).all()
        return products

    def searchById(self, id: int):
        query = select(models.Product).where(models.Product.id == id)
        product = self.session.execute(query).first()
        return product

    def edit(self, id: int, product: schemas.Product):
        update_stmt = update(models.Product).where(
            models.Product.id == id).values(nome=product.nome,
                                            detail=product.detail,
                                            price=product.price,
                                            disponible=product.disponible,
                                            )
        self.session.execute(update_stmt)
        self.session.commit()

    def delete(self, id: int):
        delete_stmt = delete(models.Product).where(
            models.Product.id == id
        )

        self.session.execute(delete_stmt)
        self.session.commit()
