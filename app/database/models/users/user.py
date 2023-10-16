from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String, Integer, Enum, Boolean, DateTime
from sqlalchemy.orm import relationship
# Locales
from app.database.config import Base
from app.routes.schemas.users.role import RoleType

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, unique=True, nullable=False)
    first_name = Column(String(30))
    last_name = Column(String(30))
    role = Column(Enum(RoleType))
    avatar = Column(String(150))
    #relaciones
    user_account = relationship('UserAccount', lazy='joined')
    user_adress = relationship('UserAdress', lazy='joined')
    stores = relationship('Store', secondary='stores_users', back_populates='users')

class UserAccount(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey('users.id_user'), nullable=False)
    username = Column(String(20), unique=True)
    password = Column(String(255))
    is_active = Column(Boolean)
    # realaciones opcionales
    user = relationship('User', back_populates='user_account', lazy='joined')

class UserAdress(Base):
    __tablename__ = 'user_adress'
    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey('users.id_user'), nullable=False)
    description = Column(String(100))
    coordinate = Column(String(100))
    # relaciones opcionales
    # user = relationship('User', back_populates='user_adress', lazy='joined')

class AccessToken(Base):
    __tablename__ = 'access_tokens'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), ForeignKey('user_account.username'), unique=True, nullable=False)
    access_token = Column(String(255))
    expiration_date = Column(DateTime(timezone=True))

    user_account = relationship('UserAccount', lazy='joined') 