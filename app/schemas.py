from pydantic import BaseModel

class QuestionBase(BaseModel):
    prompt: str
    choice_a: str
    choice_b: str
    choice_c: str
    choice_d: str
    answer: str

class QuestionCreate(QuestionBase):
    pass

class QuestionRead(QuestionBase):
    id: int
    class Config:
        from_attributes = True  # Pydantic v2 (replaces orm_mode=True)
from pydantic import BaseModel
from typing import Optional

class QuestionBase(BaseModel):
    prompt: str
    choice_a: str
    choice_b: str
    choice_c: str
    choice_d: str
    answer: str
    category: Optional[str] = None
    difficulty: Optional[str] = None
    explanation: Optional[str] = None

class QuestionCreate(QuestionBase):
    pass

class QuestionRead(QuestionBase):
    id: int
    class Config:
        from_attributes = True
