from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.data.database import Base, engine
from app.routers.question_router import router_question
from app.routers.answer_router import router_answer

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router_question)
app.include_router(router_answer)

