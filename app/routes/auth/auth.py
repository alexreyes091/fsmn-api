from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
# Locales
from app.database.config import get_db
from app.database.models.users.user import UserAccount as model_user_acount, AccessToken as model_access_token


# Proteccion de rutas:
# ---------------------------------------------
api_key_roken = APIKeyHeader(name='Token')
def protected_route(token: str = Depends(api_key_roken), db: Session = Depends(get_db)):
    # Obetenemos datos del usuario
    user = (
        db.query(model_user_acount)
        .join(model_access_token)
        .filter(model_access_token.access_token == token)
        .first()
    )

    if user is none:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='El token no es valido'
        )
