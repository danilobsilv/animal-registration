from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class UserRepositorie():

    def __init__(self, session: Session):
        self.session = session

    def create(self, user: schemas.User):
        user_bd = models.User(name=user.name,
                                    password=user.password,
                                    contact=user.contact)
        self.session.add(user_bd)
        self.session.commit()
        self.session.refresh(user_bd)
        return user_bd

    def listUsers(self):
        stmt = select(models.User)
        users = self.session.execute(stmt).scalars().all()
        return users

    def get_by_contact(self, contact) -> models.User:
        query = select(models.User).where(
            models.User.contact == contact)
        return self.session.execute(query).scalars().first()
