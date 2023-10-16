from pydantic import BaseModel, Field

class BranchBase(BaseModel):
    id: int = Field(gt=0)

    class Config:
        from_attributes = True

class Branch(BranchBase):
    branch_id: int = Field(gt=0)
    name: str = Field(min_length=5)
    adress: str = Field(max_length=100)
    description: str = Field(max_length=100)
    coordinate: str = Field()