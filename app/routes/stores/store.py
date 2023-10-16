from fastapi import FastAPI, APIRouter, Body, HTTPException, Depends, status
from sqlalchemy.orm import Session
# Locales
from app.database.config import get_db
from app.routes.stores import query_store
# Enrutador
router = APIRouter(
    prefix='/stores',
    tags=['Stores'],
)

# RUTAS STORE
# --------------------------------------------------------------------------
@router.get('/', status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_db)):
    # Obtenemos lista de todos los usuarios
    data_stores = query_store.getAll(db)

    if data_stores is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "Lista de sucursales no encontrada"
        )

    return {'stores': data_stores}


@router.get('/{id_store}', status_code=status.HTTP_200_OK)
def get(id_store: str, db: Session = Depends(get_db)):
    if id_store.isdigit():
        data_store = query_store.getStoreById(int(id_store), db)
    else: 
        data_store = None

    if data_store is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "Codigo de sucursal no encontrado."
        )

    return {'store': data_store}
# --------------------------------------------------------------------------


# STORE ASSING
# --------------------------------------------------------------------------
@router.get('/by_user_assing/{id_user}', status_code=status.HTTP_200_OK)
def get(id_user: str, db: Session = Depends(get_db)):
    if id_user.isdigit():
        user, stores = query_store.getStoresByUser(int(id_user), db)
    else: 
        user = None

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "ID de usuario no se encuentra asociado a ninguna sucursal."
        )

    return [{'user': user}, {'stores': stores}]


@router.get('/by_store_assing/{id_store}', status_code=status.HTTP_200_OK)
def get(id_store: str, db: Session = Depends(get_db)):
    if id_store.isdigit():
        store, users = query_store.getUsersByStore(int(id_store), db)
    else: 
        store = None

    if store is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "ID de sucursal no se encuentra asociado a ningun empleado."
        )

    return [{'store': store}, {'users': users}]


@router.post('/user_assing/', status_code=status.HTTP_201_CREATED)
def add(id_store: str, id_user: str, db: Session = Depends(get_db)):
    # Realiza el Post para la relacion de usuarios
    if id_store.isdigit() and id_user.isdigit():
        request = query_store.createStoreUsers(int(id_store), int(id_user), db)


@router.delete('/user_assing/', status_code=status.HTTP_200_OK)
def remove(id_store: str, id_user: str, db: Session = Depends(get_db)):
    # Realiza la eliminacion de la relacion de usuarios
    if id_store.isdigit() and id_user.isdigit():
        request = query_store.deleteStoreUsers(int(id_store), int(id_user), db)
# --------------------------------------------------------------------------
