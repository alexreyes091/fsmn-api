from pydantic import BaseModel, Field
from pydantic.types import SecretStr, constr

class Trip(BaseModel):
    id_trip: str = Field(min_length=3)
    applicant: str = Field(min_length=5)
    transport: str = Field(min_length=5)
    id_store: int = Field(gt=0)

class TripUser(BaseModel):
    id_trip: str = Field(min_length=3)
    id_user: int = Field(gt=0)