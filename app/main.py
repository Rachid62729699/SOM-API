from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from .db import Base, engine, SessionLocal
from . import models, schemas

load_dotenv()
app = FastAPI(title="SOM API", version="0.1.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"healthy": True}

@app.post("/questions", response_model=schemas.QuestionRead)
def create_question(q: schemas.QuestionCreate, db: Session = Depends(get_db)):
    data = q.model_dump() if hasattr(q, "model_dump") else q.dict()
    obj = models.Question(**data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@app.get("/questions", response_model=list[schemas.QuestionRead])
def list_questions(db: Session = Depends(get_db)):
    return db.query(models.Question).all()

