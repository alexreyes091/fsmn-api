from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
# 
# Routers de la API
from app.database.config import Base, engine
from app.routes.users.user import router as user_router
from app.routes.stores.store import router as store_router
from app.routes.trips.trip import router as trip_router
from app.routes.transport.transport import router as transport_router
# Modelos de bases de datos
from app.database.models.users.user import User
from app.database.models.stores.store import Store
from app.database.models.transports.transport import Transport
from app.database.models.trips.trip import Trip
# Instancias para data de ejemplo
from app.database.models.users.data_example import init_db as init_db_users
from app.database.models.stores.data_example import init_db as init_db_stores
from app.database.models.transports.data_example import init_db as init_db_transport
# Instancia
app = FastAPI()
# Control de CROS POLICY
origins = [
    "http://127.0.0.1:5173", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Creamos todos los modelos
Base.metadata.create_all(bind=engine)
# Cargar datos inciales
try:
    # TODO: Cambiar esta forma de crear las tablas.
    init_db_users()
    init_db_stores()
    init_db_transport()
except:
    print('Error al tratar de crear las bases de datos, puede que ya existan.')
# Listado de rutas
app.include_router(user_router)
app.include_router(store_router)
app.include_router(transport_router)
app.include_router(trip_router)