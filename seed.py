from app.db import Base, engine, SessionLocal
from app.models import Question

Base.metadata.create_all(bind=engine)

db = SessionLocal()
try:
    if not db.query(Question).first():
        samples = [
            Question(prompt="What is 2 + 2?", choice_a="3", choice_b="4",
                     choice_c="5", choice_d="6", answer="B"),
            Question(prompt="Simplify: 3^2 × 3^3 = ?", choice_a="3^5",
                     choice_b="3^6", choice_c="3^1", choice_d="3^9", answer="A"),
            Question(prompt="If x + 5 = 12, what is x?",
                     choice_a="5", choice_b="6", choice_c="7", choice_d="17", answer="C"),
        ]
        db.add_all(samples)
        db.commit()
finally:
    db.close()
