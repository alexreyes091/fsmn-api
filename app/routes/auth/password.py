import secrets
from passlib.context import CryptContext

# Funciones para control de password
# -------------------------------------------------------------------
context = CryptContext(schemes=['bcrypt'])

def get_password_hash(password: str) -> str:
    return context.hash(password)

def verify_password(plain_password: str, password: str) -> bool:
    return context.verify(plain_password, password)

def generate_token() -> str:
    return secrets.token_urlsafe(32) #32 numero de bites