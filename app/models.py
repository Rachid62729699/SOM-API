from sqlalchemy import Column, Integer, String, Text
from .db import Base

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text, nullable=False)
    choice_a = Column(String(255), nullable=False)
    choice_b = Column(String(255), nullable=False)
    choice_c = Column(String(255), nullable=False)
    choice_d = Column(String(255), nullable=False)
    answer = Column(String(1), nullable=False)  # "A" / "B" / "C" / "D"
from sqlalchemy import Column, Integer, String, Text
from .db import Base

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text, nullable=False)
    choice_a = Column(String(255), nullable=False)
    choice_b = Column(String(255), nullable=False)
    choice_c = Column(String(255), nullable=False)
    choice_d = Column(String(255), nullable=False)
    answer  = Column(String(1), nullable=False)  # "A"/"B"/"C"/"D"
    category = Column(String(50), nullable=True)     # e.g. "exponents"
    difficulty = Column(String(20), nullable=True)   # "easy|med|hard"
    explanation = Column(Text, nullable=True)
