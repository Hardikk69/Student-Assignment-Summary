from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DB_URL="postgresql://postgres:123@localhost:5432/Student_assignment_system"
Engine=create_engine(DB_URL)

SessionLocal=sessionmaker(autoflush=False,bind=Engine)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_table():
    Base.metadata.create_all(bind=Engine)

def drop_table():
    Base.metadata.drop_all(bind=Engine)

