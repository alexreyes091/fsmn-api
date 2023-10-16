from enum import Enum
from pydantic import BaseModel, Field

class RoleType(str, Enum):
    MANAGER = 'manager'
    COLABORADOR = 'colaborador'

# class Role(BaseModel):
#     id: int = Field(gt=0)
#     role: RoleType