from pydantic import BaseModel, ConfigDict
from datetime import datetime

class AnswerCreate(BaseModel):
    question_id: int
    user_id: int
    text: str
    created_at: datetime

class AnswerOut(BaseModel):
    id: int
    question_id: int
    user_id: int
    text: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)