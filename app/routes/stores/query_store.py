from fastapi import HTTPException, status
from sqlalchemy.orm import Session
#Locales
from app.database.models.stores.store import Store as model_store, stores_users
from app.routes.users.query_user import isUserExist, getUserById

# STORES
# -------------------------------------------------------------
def getAll(db: Session):
    store = db.query(model_store).all()
    return store

def getStoreById(id_store: int, db: Session):
    store = (
        db.query(model_store)
        .filter(model_store.id_store == id_store)
        .first()
    )
    return store
# -------------------------------------------------------------


# STORES ASSIGN
# -------------------------------------------------------------
def getStoresByUser(user_id: int, db: Session):
    # Obtiene la lista de sucursales por cada usuarios
    if isUserExist(user_id, db):
        # Query para obtener las stores por usuario
        stores_by_user = (
            db.query(stores_users)
            .filter_by(id_user = user_id)
            .all()
        )
        # Construyendo el request
        data_user = getUserById(user_id, db)
        data_stores_assing = []

        for id_store, id_user in stores_by_user:
            data_stores_assing.append(getStoreById(id_store, db))

        return data_user, data_stores_assing
    return None, None


def getUsersByStore(store_id: int, db: Session):
    # Obtiene la lista de usuarios por cada sucursal
    if isStoreExist(store_id, db):
        # Query para obtener las stores por usuario
        users_by_store = (
            db.query(stores_users)
            .filter_by(id_store = store_id)
            .all()
        )
        # Construyendo el request
        data_store = getStoreById(store_id, db)
        data_users_assing = []

        for id_store, id_user in users_by_store:
            data_users_assing.append(getUserById(id_user, db))

        return data_store, data_users_assing
    return None, None


def createStoreUsers(id_store: int, id_user: int, db: Session):
    # Crea la realcion de sucursal y usuarios
    if isUserExist(id_user, db) and isStoreExist(id_store, db):

        user = getUserById(id_user, db)
        store = getStoreById(id_store, db)

        if user in store.users:
            raise HTTPException(
                status_code = status.HTTP_406_NOT_ACCEPTABLE,
                detail = 'El usuario ya esta asignado a esta surcursal.'
            )
        store.users.append(user)
        db.commit()

        raise HTTPException(
            status_code = status.HTTP_201_CREATED,
            detail = 'Registro creado correctamente'
        )
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Los registros de usuario y/o sucursal no se encontraron."
    )


def deleteStoreUsers(id_store: int, id_user: int, db: Session):
    # Elimina la realcion de sucursal y usuarios
    if isUserExist(id_user, db) and isStoreExist(id_store, db):

        user = getUserById(id_user, db)
        store = getStoreById(id_store, db)

        if not user in store.users:
            raise HTTPException(
                status_code = status.HTTP_200_OK,
                detail = 'El usuario no esta asignado a esta surcursal.'
            )

        store.users.remove(user)
        db.commit()

        raise HTTPException(
            status_code = status.HTTP_201_CREATED,
            detail = 'Registro eliminado correctamente'
        )
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Los registros de usuario y/o sucursal no se encontraron."
    )
# -------------------------------------------------------------


# VALIDACIONES
# -------------------------------------------------------------
def isStoreExist(id_store: int, db: Session):
    store = (
        db.query(model_store)
        .filter(model_store.id_store == id_store)
        .first()
    )
    return store is not None