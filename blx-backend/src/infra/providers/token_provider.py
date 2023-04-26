from datetime import datetime, timedelta
from jose import jwt

# CONFIG
SECRET_KEY = 'caa9c8f8620cbb30679026bb6427e11f'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000


def create_access_token(data: dict):
    data = data.copy()
    expire_time = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    data.update({'exp': expire_time})

    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verify_access_token(token: str):
    cargo = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return cargo.get('sub')
