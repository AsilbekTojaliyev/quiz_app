from pydantic import BaseModel, Field


class CreateQuestion(BaseModel):
    question: str
    category_id: int = Field(..., gt=0)


class UpdateQuestion(BaseModel):
    ident: int = Field(...,gt=0)
    question: str
    category_id: int = Field(..., gt=0)
