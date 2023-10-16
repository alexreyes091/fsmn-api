import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
#Locales
from app.database.models.trips.trip import Trip as model_trip, trip_users
from app.routes.users.query_user import isUserExist, getUserById
# from app.database.models.stores.store import Store as model_store, stores_users
# from app.routes.users.query_user import isUserExist, getUserById

# TRIPS 
# -------------------------------------------------------------
def getAll(db: Session):
    try:
        trips = db.query(model_trip).all()
        return trips
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "El registro del viaje no fue encontrado."
        )


def getTripById(id_trip: int, db: Session):
    try:
        trip = (
            db.query(model_trip)
            .filter(model_trip.id_trip == id_trip)
            .first()
        )
        if trip:
            return trip
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail = "El registro del viaje no fue encontrado."
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "El registro del viaje no fue encontrado."
        )
        

# TODO: Crear esquemas pydentic
def createTrip(id_trip: int, applicant: str, licence_plate: str, id_store: int, date: datetime, db: Session):

    # Validamos si el transportista y la sucursal existen.
    if isTransportExist(licence_plate, db) and isStoreExist(id_store, db):

        if not getTripById(id_trip, db):
            trip = model_trip(
                id_trip = id_trip,
                applicant = applicant,
                transport = licence_plate,
                id_store = id_store,
                created_date = date,
            )
            
            print(trip)

            db.add(trip)
            db.commit()

            raise HTTPException(
                status_code = status.HTTP_201_CREATED,
                detail = 'Registro creado correctamente.'
            )
        else:
            raise HTTPException(
                status_code = status.HTTP_406_NOT_ACCEPTABLE,
                detail = 'El registro de este viaje ya existe.'
            )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Los registros de transporte y/o sucursal no se encontraron."
    )


def updateTrip(id_trip: int, applicant: str, licence_plate: str, id_store: int, date: datetime, db: Session):
    # Validamos si el transportista y la sucursal existen.
    if isTransportExist(licence_plate, db) and isStoreExist(id_store, db):
        # Recuperamos el viaje que queremos actualizar
        dbTrip = getTripById(id_trip, db)

        if dbTrip:
            dbTrip.id_trip = id_trip,
            dbTrip.applicant = applicant,
            dbTrip.transport = licence_plate,
            dbTrip.id_store = id_store,
            dbTrip.created_date = date

            db.add(dbTrip)
            db.commit()
            # Actualiza la instancia de la db en general, tipo id o datos relacionados.
            db.refresh(dbTrip)

            raise HTTPException(
                status_code = status.HTTP_200_OK,
                detail = 'Registro actualizado correctamente.'
            )
        else:
            raise HTTPException(
                status_code = status.HTTP_406_NOT_ACCEPTABLE,
                detail = 'El registro de este viaje no extiste.'
            )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Los registros de transporte y/o sucursal no se encontraron."
    )
# -------------------------------------------------------------


# TRIP ASSIGN
# -------------------------------------------------------------
def getTripsByUser(user_id: int, db: Session):
    # Obtiene la lista de sucursales por cada usuarios
    if isUserExist(user_id, db):
        # Query para obtener los trips por usuario
        trip_by_user = (
            db.query(trip_users)
            .filter_by(id_user = user_id)
            .all()
        )
        # Construyendo el request
        data_user = getUserById(user_id, db)
        data_trip_assing = []

        for id_trip, id_user in trip_by_user:
            data_trip_assing.append(getTripById(id_trip, db))

        return data_user, data_trip_assing
    return None, None


def getUsersByTrip(trip_id: int, db: Session):
    # Obtiene la lista de usuarios por cada sucursal
    if isTripExist(trip_id, db):
        # Query para obtener las viajes por usuario
        users_by_store = (
            db.query(trip_users)
            .filter_by(id_trip = trip_id)
            .all()
        )
        # Construyendo el request
        data_trip = getTripById(trip_id, db)
        data_users_assing = []

        for id_trip, id_user in users_by_store:
            data_users_assing.append(getUserById(id_user, db))

        return data_trip, data_users_assing
    return None, None


def createTripUsers(id_trip: int, id_user: int, db: Session):
     # Crea la realcion de sucursal y usuarios
    if isUserExist(id_user, db) and isTripExist(id_trip, db):

        user = getUserById(id_user, db)
        trip = getTripById(id_trip, db)

        if user in trip.users:
            raise HTTPException(
                status_code = status.HTTP_406_NOT_ACCEPTABLE,
                detail = 'El usuario ya esta asignado en este viaje.'
            )
        
        # TODO: Realizar restriccion de usuarios viajaran solo asignados a la sucrusal asignada.
        trip.users.append(user)
        db.commit()

        raise HTTPException(
            status_code = status.HTTP_201_CREATED,
            detail = 'Registro creado correctamente'
        )
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Los registros de viaje y/o usuarios no se encontraron."
    )

def deleteTripUsers(id_trip: int, id_user: int, db: Session):
    # Elimina la realcion de sucursal y usuarios
    if isUserExist(id_user, db) and isTripExist(id_trip, db):

        user = getUserById(id_user, db)
        trip = getTripById(id_trip, db)

        if not user in trip.users:
            raise HTTPException(
                status_code = status.HTTP_200_OK,
                detail = 'El usuario no esta asignado a este viaje.'
            )

        trip.users.remove(user)
        db.commit()

        raise HTTPException(
            status_code = status.HTTP_201_CREATED,
            detail = 'Registro eliminado correctamente'
        )
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Los registros de usuario y/o sucursal no se encontraron."
    )

# VALIDACIONES
# -------------------------------------------------------------
def isTripExist(id_trip: int, db: Session):
    trip = (
        db.query(model_trip)
        .filter(model_trip.id_trip == id_trip)
        .first()
    )
    return trip is not None