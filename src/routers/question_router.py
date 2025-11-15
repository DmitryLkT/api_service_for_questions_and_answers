from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
import datetime

from src.schemas.question_schema import QuestionOut
from src.schemas.question_schema import QuestionCreate
from src.schemas.answer_schema import AnswerCreate
from src.models.answer_model import Answer
from src.models.question_model import Question
from src.data.database import get_db

router = APIRouter(prefix="/question", tags=["question"])

@router.get("/", response_model=list[QuestionOut])
def read_questions(db: Session = Depends(get_db)):
    return db.query(Question).all()

@router.get("/{id}", response_model=QuestionOut)
def read_question(id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == id).first()

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    return question

@router.post("/", response_model=QuestionCreate)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    db_question = Question(text=question.text, created_at=datetime.now())
    db.add(db_question)
    db.commit()

@router.post("/{id}/answer", response_model=AnswerCreate)
def create_answer(id: int, answer: AnswerCreate, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == id).first()

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    db_answer = Answer(question_id=id, text=answer.text, created_at=datetime.now())
    db.add(db_answer)
    db.commit()


@router.delete("/{id}")
def delete_question(id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == id).first()

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    db.delete(question)
    db.commit()