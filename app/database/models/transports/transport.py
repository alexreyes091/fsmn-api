from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Float
# Locales
from app.database.config import Base

class Transport(Base):
    __tablename__ = "transport"
    id = Column(Integer, primary_key=True, index=True)
    licence_plate = Column(String, unique=True)
    rate = Column(Float)
    driver = Column(String(100))
