from app.database.models.stores.store import Store
from app.database.config import SessionLocal
# Carga de datos incial
def init_db():
    db = SessionLocal()
    # Instancias de datos
    stores = seed_stores()
    # Carga de datos
    db.add_all(stores)
    db.commit()

# Semilla de datos iniciales
def seed_stores():
    stores = [
        Store(id_store=51, name='FARSIMAN', adress='Avenida Circunvalacion, San Pedro Sula', coordinate='-88.03795390269629,15.503498380878014'),
        Store(id_store=52, name='SUPER FARSIMAN', adress='Super Farmacia Siman, Barrio El Benque, San Pedro Sula', coordinate='-88.02709890755573,15.502475909458724'),
        Store(id_store=53, name='FARSIMAN', adress='Farmacia Siman Texaco Villa Olimpica, 2do Anillo Periferico 20 Calle', coordinate='-88.00584562526991,15.484272728189993'),
        Store(id_store=54, name='FARMACIA SIMAN', adress='Farmacia Siman Colonial 2, Blvd del Norte, San Pedro Sula', coordinate='-88.00480315347622,15.550366672926941'),
        Store(id_store=55, name='FARSIMAN CHLM', adress='Bo. El Centro, frente al parque de Choloma', coordinate='-87.95247482438242,15.612145035957624'),
    ]
    return stores
