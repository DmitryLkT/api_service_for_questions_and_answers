from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.answer_schema import AnswerOut
from app.data.database import get_db
from app.models.answer_model import Answer

router_answer = APIRouter(prefix="/answers", tags=["Answers"])

@router_answer.get("/{id}", response_model=AnswerOut)
def get_answer(id: int, db: Session = Depends(get_db)):
    answer = db.query(Answer).filter(Answer.id == id).first()

    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    return answer

@router_answer.delete("/{id}")
def delete_answer(id: int, db: Session = Depends(get_db)):
    answer = db.query(Answer).filter(Answer.id == id).first()

    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    db.delete(answer)
    db.commit()