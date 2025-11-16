import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.data.database import Base, get_db
from app.models.question_model import Question

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture()
def test_db():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

def test_read_questions(test_db):
    db = TestSessionLocal()

    q1 = Question(text="First question", created_at="2025-11-15T10:00:00")
    q2 = Question(text="Second question", created_at="2025-11-15T10:00:00")

    db.add(q1)
    db.add(q2)
    db.commit()
    db.close()

    response = client.get("/questions")

    assert response.status_code == 200
    data=response.json()

    assert len(data) == 2
    assert data[0]["text"] == "First question"
    assert data[1]["text"] == "Second question"

    assert data[0]["id"] >= 1
