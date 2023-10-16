from fastapi import FastAPI, APIRouter, HTTPException, Depends, status
from fastapi.security import APIKeyHeader, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Union
# Locales
from app.database.models.users.user import UserAccount as model_user_acount, AccessToken as model_access_token
from app.database.config import get_db
from app.routes.users import query_user
from app.routes.auth import password as password_auth, authtentication
from app.routes.auth.auth import protected_route
from app.routes.auth.authtentication import authenticate, create_access_token, get_token_access, verify_access_token
# Esquemas
from app.routes.schemas.users.user import LoginData
# Enrutador
router = APIRouter(
    prefix='/users',
    tags=['Users'],
)

# ROUTES
# ---------------------------------------------------------
# @router.get('/', status_code=status.HTTP_200_OK)
# def get(user = Depends(verify_access_token), db: Session = Depends(get_db)):
@router.get('/', status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_db)):
    # Obtenemos lista de todos los usuarios
    data_users = query_user.getAll(db)

    if data_users:
        return {'users': data_users}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "Lista de usuarios no encontrada"
        )

@router.get('/{id_user}', status_code=status.HTTP_200_OK)
def get(id_user: str, db: Session = Depends(get_db)):
    if id_user.isdigit():
        # Obtenemos datos del usuario
        data_user = query_user.getUserById(int(id_user), db)
    else: 
        data_user = None

    if data_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "Codigo de usuario no encontrado."
        )
        
    return {'user': data_user}


# Sistema de LOGIN
# ---------------------------------------------------------
@router.post('/login')
def login(login_data: LoginData, db: Session = Depends(get_db)):
    # Obtenemos el usuario logueado
    username = login_data.username
    password = login_data.password
    user_login = authenticate(username, password, db)
    # Validamos si es valido
    if user_login is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Usuario y contrasena no son validos'
        )
    # Obtenemos el tocken para validarlo
    user_acces_token = get_token_access(user_login.username, db)
    if user_acces_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Su acceso ha sido dado de baja.'
        )
        
    data_account = verify_access_token(user_acces_token.access_token, db)

    return data_account

# ! Realizar control de token si existe o si estara vencido para que genere otro
@router.post('/token')
def crear_token(
    form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm), 
    db: Session = Depends(get_db)):
    # Obtenemos los datos
    username = form_data.username
    password = form_data.password
    # Validamos
    user = authtentication.authenticate(username, password, db)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Usuario y contrasena no son validos'
        )
    # Crea el token 
    token = create_access_token(user, db)
    
    return {'access_token': token.access_token}
    


@router.post('/register', status_code=status.HTTP_201_CREATED)
def register(id_user: int, username: str, password: str, is_active: bool, db: Session = Depends(get_db)): # -> model_user_acount
    
    # Validamos si el username ya existe
    user_exist = (
        db.query(model_user_acount)
        .filter(model_user_acount.username == username)
        .first()
    )

    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="La cuenta ingresada ya se encuentra registrada"
        )

    hash_psw = password_auth.get_password_hash(password)
    user_db = model_user_acount(id_user = id_user, 
                                username=username,
                                password=hash_psw,
                                is_active=True)
    
    # TODO: Separar la logica de la ruta
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db