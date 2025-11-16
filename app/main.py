from fastapi import FastAPI
import uvicorn

from src.data.database import Base, engine
from src.routers.question_router import router_question
from src.routers.answer_router import router_answer

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_question)
app.include_router(router_answer)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
