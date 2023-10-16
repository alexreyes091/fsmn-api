from fastapi import FastAPI, APIRouter, Body, HTTPException, Depends, status
from sqlalchemy.orm import Session
# Locales
from app.database.config import get_db
from app.routes.transport import query_transport
# Enrutador
router = APIRouter(
    prefix='/transport',
    tags=['Transport'],
)

# RUTAS TRNASPORT 
# -------------------------------------------------------------
@router.get('/', status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_db)):
    # Obtenemos lista de todos los usuarios
    data_transport = query_transport.getAll(db)

    if data_transport is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "Lista de sucursales no encontrada"
        )

    return {'transport': data_transport}


@router.get('/{licence_plate}', status_code=status.HTTP_200_OK)
def get(licence_plate: str, db: Session = Depends(get_db)):
    # Obtenemos el transporte por su numero de placa
    data_transport = query_transport.getTransportById(licence_plate, db)

    if data_transport is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "Numero de palca no encontrado."
        )

    return {'transport': data_transport}
# -------------------------------------------------------------

