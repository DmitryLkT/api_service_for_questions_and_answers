from sqlalchemy.orm import Session, joinedload
from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime

from app.schemas.question_schema import QuestionOut, QuestionCreate
from app.schemas.answer_schema import AnswerCreate, AnswerOut
from app.models.answer_model import Answer
from app.models.question_model import Question
from app.data.database import get_db

router_question = APIRouter(prefix="/questions", tags=["question"])

@router_question.get("/", response_model=list[QuestionOut])
def read_questions(db: Session = Depends(get_db)):
    return db.query(Question).all()

@router_question.get("/{id}", response_model=QuestionOut)
def read_question(id: int, db: Session = Depends(get_db)):
    question = db.query(Question).options(joinedload(Question.answers)).filter(Question.id == id).first()

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    return question

@router_question.post("/", response_model=QuestionOut)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    db_question = Question(text=question.text, created_at=datetime.now())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

@router_question.post("/{id}/answers", response_model=AnswerOut)
def create_answer(id: int, answer: AnswerCreate, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == id).first()

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    db_answer = Answer(question_id=id, text=answer.text, created_at=datetime.now())
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


@router_question.delete("/{id}")
def delete_question(id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == id).first()

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    db.delete(question)
    db.commit()