from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List

from src.schemas.answer_schema import AnswerOut

class QuestionCreate(BaseModel):
    text: str

class QuestionOut(BaseModel):
    id: int
    text: str
    created_at: datetime
    answers: List[AnswerOut] = []

    model_config = ConfigDict(from_attributes=True)