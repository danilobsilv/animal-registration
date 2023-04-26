from src.infra.sqlalchemy.repositories.user_repo import UserRepositorie
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette import status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider
from jose import JWTError

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def get_logged_user(token: str = Depends(oauth2_schema),
                         session: Session = Depends(get_db)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

    try:
        contact = token_provider.verify_access_token(token)
    except JWTError:
        raise exception

    if not contact:
        raise exception

    user = UserRepositorie(session).get_by_contact(contact)

    if not user:
        raise exception

    return user
