from pydantic import BaseModel, Field

# Locales
class StoreUsers(BaseModel):
    id_store: str = Field()
    id_user: str = Field()
    distance: str = Field()