from datetime import datetime
from fastapi import FastAPI, APIRouter, Body, HTTPException, Depends, status
from sqlalchemy.orm import Session, load_only
# Locales
from app.database.config import get_db
from app.routes.trips import query_trip
# Enrutador
router = APIRouter(
    prefix='/trips',
    tags=['Trips'],
)
# Rutas Trips
# --------------------------------------------------------
@router.get('/', status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_db)):
    # Obtenemos lista de trips
    request = query_trip.getAll(db)
    return request


@router.get('/{id_trip}', status_code=status.HTTP_200_OK)
def get(id_trip: str, db: Session = Depends(get_db)):
    # Obtenemos lista de trips
    if id_trip.isdigit():
        # Obtenemos datos del usuario
        request = query_trip.getTripById(id_trip, db)
    else: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "Registro de viaje no valido."
        )

    return request


# TODO: Crear esquemas pydentic
@router.post('/', status_code=status.HTTP_200_OK)
def create(id_trip: int, applicant: str, licence_plate: str, id_store: int, date: datetime, db: Session = Depends(get_db)):
    # Obtenemos lista de trips
    request = query_trip.createTrip(id_trip, applicant, licence_plate, id_store, date, db)

    return request

# TODO: Crear esquemas pydentic
@router.put('/', status_code=status.HTTP_200_OK)
def update(id_trip: int, applicant: str, licence_plate: str, id_store: int, date: datetime, db: Session = Depends(get_db)):
    # Obtenemos lista de trips
    request = query_trip.updateTrip(id_trip, applicant, licence_plate, id_store, date, db)

    return request

# RUTAS TRIPS-USER ASSING
#----------------------------------------------------------------------------------
@router.get('/by_user_assing/{id_user}', status_code=status.HTTP_200_OK)
def get(id_user: str, db: Session = Depends(get_db)):
    if id_user.isdigit():
        user, trips = query_trip.getTripsByUser(int(id_user), db)
    else: 
        user = None

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "ID de usuario no se encuentra asociado a ningun viaje."
        )

    return [{'user': user}, {'trips': trips}]


@router.get('/by_trip_assing/{id_trip}', status_code=status.HTTP_200_OK)
def get(id_trip: str, db: Session = Depends(get_db)):
    if id_trip.isdigit():
        trip, users = query_trip.getUsersByTrip(int(id_trip), db)
    else: 
        trip = None

    if trip is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "ID de sucursal no se encuentra asociado a ningun empleado."
        )

    return [{'trip': trip}, {'users': users}]

    
@router.post('/user_assing/', status_code=status.HTTP_201_CREATED)
def add(id_trip: str, id_user: str, db: Session = Depends(get_db)):
    # Realiza el Post para la relacion de usuarios
    if id_trip.isdigit() and id_user.isdigit():
        request = query_trip.createTripUsers(int(id_trip), int(id_user), db)


@router.delete('/user_assing/', status_code=status.HTTP_200_OK)
def remove(id_trip: str, id_user: str, db: Session = Depends(get_db)):
    # Realiza la eliminacion de la relacion de usuarios
    if id_trip.isdigit() and id_user.isdigit():
        request = query_trip.deleteTripUsers(int(id_trip), int(id_user), db)
# --------------------------------------------------------

