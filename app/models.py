# app/models.py
from sqlalchemy import Column, Integer, String, Text
from .db import Base                      # <-- import Base from db.py

class Question(Base):
    __tablename__ = "questions"
    # __table_args__ = {"extend_existing": True}  # (only if you still see the error)
    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text, nullable=False)
    choice_a = Column(String(255), nullable=False)
    choice_b = Column(String(255), nullable=False)
    choice_c = Column(String(255), nullable=False)
    choice_d = Column(String(255), nullable=False)
    answer = Column(String(1), nullable=False)
    category = Column(String(50), nullable=True)
    difficulty = Column(String(20), nullable=True)
    explanation = Column(Text, nullable=True)
