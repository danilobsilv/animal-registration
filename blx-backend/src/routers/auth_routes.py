from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import LoginSucess, User, SimpleUser, LoginData
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.user_repo import UserRepositorie
from src.infra.providers import hash_provider, token_provider
from src.routers.auth_utils import get_logged_user

router = APIRouter()


@router.post('/signup',
             status_code=status.HTTP_201_CREATED,
             response_model=SimpleUser)
def signup(user: User, session: Session = Depends(get_db)):

    user_found = UserRepositorie(
        session).get_by_contact(user.contact)

    if user_found:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='A user already exists for this contact')

    user.password = hash_provider.generate_hash(user.password)
    user_created = UserRepositorie(session).create(user)
    return user_created


@router.post('/token', response_model=LoginSucess)
def login(login_data: LoginData, session: Session = Depends(get_db)):
    password = login_data.password
    contact = login_data.contact

    user = UserRepositorie(session).get_by_contact(contact)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='contact or password are not correct!')

    valid_password = hash_provider.verify_hash(password, user.password)
    if not valid_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='contact or password are not correct!')
  
    token = token_provider.create_access_token({'sub': user.contact})
    return LoginSucess(user=user, access_token=token)


@router.get('/me', response_model=SimpleUser)
def me(user: User = Depends(get_logged_user)):
    return user
