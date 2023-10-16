from datetime import datetime, timedelta, timezone  
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
# Locales
from app.database.config import get_db
from app.database.models.users.user import UserAccount as model_user, AccessToken
from app.database.models.users.user import UserAccount as model_user_acount, AccessToken as model_access_token
from app.routes.auth.password import verify_password, generate_token


def get_token_access(username: str, db: Session):
    token = (
         db.query(model_access_token)
         .filter(model_access_token.username == username)
         .first()
    )

    return token

def authenticate(username: str, password: str, db: Session) -> model_user | None:
    user = db.query(model_user).filter(model_user.username == username).first()
    # Verificaciones
    if user is None:
        return None

    if not verify_password(password, user.password):
        return None

    return user


def create_access_token(user: model_user, db: Session) -> AccessToken:
    time = datetime.now() + timedelta(days=60)
    # Creamos el access token
    accessToken = AccessToken(username=user.username, access_token=generate_token(), expiration_date=time,)

    # Almacenamos en la base de datos
    db.add(accessToken)
    db.commit()
    db.refresh(accessToken)

    return accessToken


api_key_roken = APIKeyHeader(name='Token')
def verify_access_token(token: str = Depends(api_key_roken), db: Session = Depends(get_db)):
    # Obetenemos datos del usuario
    access_token = (
        db.query(model_access_token)
        .join(model_user_acount)
        .filter(model_access_token.access_token == token)
        .first()
    )

    if access_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='El token no es valido'
        )

    if datetime.now(timezone.utc) > access_token.expiration_date:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='El token no es valido'
        )
    
    return access_token