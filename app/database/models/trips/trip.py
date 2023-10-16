import datetime
from sqlalchemy.schema import Column, ForeignKey, Table
from sqlalchemy.types import String, Integer, Enum, Boolean, DateTime
from sqlalchemy.orm import relationship
# Locales
from app.database.config import Base

# Tabla de union para mantener relacion entre usuarios y viajes
trip_users = Table(
    'trip_users',
    Base.metadata,
    Column('id_trip', Integer, ForeignKey('trips.id_trip'), primary_key=True),
    Column('id_user', Integer, ForeignKey('users.id_user'), primary_key=True),
)

class Trip(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True, index=True)
    id_trip = Column(Integer, unique=True, nullable=False)
    applicant = Column(String(60), nullable=False)
    transport = Column(String, ForeignKey('transport.licence_plate'), nullable=False)
    id_store = Column(Integer, ForeignKey('stores.id_store'), nullable=False)
    created_date = Column(DateTime)
    
    users = relationship('User', secondary='trip_users')