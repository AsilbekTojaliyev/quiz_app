from pydantic import BaseModel, Field


class CreateResult(BaseModel):
    category_id: int = Field(..., gt=0)
    question_id: int = Field(..., gt=0)
    answer_id: int = Field(..., gt=0)
