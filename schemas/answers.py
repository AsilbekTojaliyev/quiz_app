from pydantic import BaseModel, Field


class CreateAnswer(BaseModel):
    answer: str
    status: bool
    question_id: int = Field(..., gt=0)


class UpdateAnswer(BaseModel):
    ident: int = Field(..., gt=0)
    answer: str
    status: bool
    question_id: int = Field(..., gt=0)
