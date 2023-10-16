from app.database.models.transports.transport import Transport
from app.database.config import SessionLocal

# Carga de datos incial
def init_db():
    db = SessionLocal()
    # Instancias de datos
    transport = seed_transport()
    # Carga de datos
    db.add_all(transport)
    db.commit()

# Semilla de datos iniciales
def seed_transport():
    transport = [
        Transport(licence_plate='HAA-1234', rate=10.55, driver='Felipe Izaguirre Montoya'),
        Transport(licence_plate='HND-5678', rate=11.23, driver='Pedro Alberto Juarez'),
        Transport(licence_plate='HGU-9012', rate=13.11, driver='Jose Antonio Bueso'),
        Transport(licence_plate='HPS-3456', rate=10.33, driver='Pedro Alberto Juarez'),
        Transport(licence_plate='HPS-7890', rate=15.89, driver='Pedro Alberto Juarez'),
    ]
    return transport
