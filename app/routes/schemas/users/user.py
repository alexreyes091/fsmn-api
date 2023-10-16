from enum import Enum
from pydantic import BaseModel, Field
from pydantic.types import SecretStr, constr
# Locales
from .role import RoleType

class LoginData(BaseModel):
    username: str = Field()
    password: str = Field()

class UserAdress(BaseModel):
    description: str = Field(max_length=100)
    coordinate: str = Field()

class UserAdress(BaseModel):
    description: str = Field(max_length=100)
    coordinate: str = Field()

class UserAccount(BaseModel):
    username: constr(to_lower=True)
    password: SecretStr

class User(BaseModel):
    id_user: int = Field(gt=0)
    first_name: str = Field(min_length=5)
    last_name: str = Field(min_length=5)
    user_account: UserAccount
    user_adress: UserAdress
    role: RoleType
