# init_db.py
from Database import Base, Engine
from Models import Admin_table, Teacher, Subject, Student, Summarizer

Base.metadata.drop_all(bind=Engine)
Base.metadata.create_all(bind=Engine)
print("All tables created successfully.")
