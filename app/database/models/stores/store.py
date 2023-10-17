from sqlalchemy.schema import Column, ForeignKey, Table
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship
# Locales
from app.database.config import Base
from app.database.models.users.user import User

# Tabla de union para mantener relacion entre usuarios y sucursales
stores_users = Table(
    'stores_users',
    Base.metadata,
    Column('id_store', Integer, ForeignKey('stores.id_store'), primary_key=True),
    Column('id_user', Integer, ForeignKey('users.id_user'), primary_key=True),
    Column('distance', String(50), nullable=False)
)

class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True, index=True)
    id_store = Column(Integer, unique=True, nullable=False)
    name = Column(String(100)) 
    adress = Column(String(100))
    coordinate = Column(String(100))

    users = relationship('User', secondary='stores_users', back_populates='stores')
