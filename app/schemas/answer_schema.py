from pydantic import BaseModel, ConfigDict
from datetime import datetime
from uuid import UUID

class AnswerCreate(BaseModel):
    text: str

class AnswerOut(BaseModel):
    id: int
    question_id: int
    user_id: UUID
    text: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)