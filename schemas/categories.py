from pydantic import BaseModel, Field


class CreateCategory(BaseModel):
    category: str


class UpdateCategory(BaseModel):
    ident: int = Field(..., gt=0)
    category: str
