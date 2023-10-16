from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://alexreyes:GimTextR5B@localhost:5434/thw-db'
engine = create_engine(DATABASE_URL)

#Se necesita la sesion para crear la conexion
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally: 
        db.close()