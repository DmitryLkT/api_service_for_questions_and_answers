from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from src.data.database import Base

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    user_id = Column(UUID(as_uuid=True), default=uuid.uuid4())
    text = Column(String, nullable=False)
    created_at = Column(String, nullable=False)

