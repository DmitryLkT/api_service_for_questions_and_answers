from src.data.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    created_at = Column(String, nullable=False)

    answers = relationship("Answer", cascade="all, delete", backref="question")