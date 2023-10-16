from sqlalchemy.orm import Session
#Locales
from app.database.models.transports.transport import Transport as model_transport

# TRANSPORT
# -------------------------------------------------------------
def getAll(db: Session):
    transport = db.query(model_transport).all()
    return transport


def getTransportById(licence_plate: int, db: Session):
    transport = (
        db.query(model_transport)
        .filter(model_transport.licence_plate == licence_plate)
        .first()
    )
    return transport
# -------------------------------------------------------------

    
# VALIDACIONES 
# -------------------------------------------------------------
def isTransportExist(licence_plate: int, db: Session):
    transport = (
        db.query(model_transport)
        .filter(model_transport.licence_plate == licence_plate)
        .first()
    )
    return transport is not None