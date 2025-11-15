from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.schemas.answer_schema import AnswerOut
from src.data.database import get_db
from src.models.answer_model import Answer

router = APIRouter(prefix="/answers", tags=["Answers"])

@router.get("/{id}", response_model=AnswerOut)
def get_answer(id: int, db: Session = Depends(get_db)):
    answer = db.query(Answer).filter(Answer.id == id).first()

    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    return answer

@router.delete("/{id}", response_model=AnswerOut)
def delete_answer(id: int, db: Session = Depends(get_db)):
    answer = db.query(Answer).filter(Answer.id == id).first()

    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    db.delete(answer)
    db.commit()