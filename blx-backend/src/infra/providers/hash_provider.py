from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])


def generate_hash(text):
    return pwd_context.hash(text)


def verify_hash(text, hash):
    return pwd_context.verify(text, hash)
