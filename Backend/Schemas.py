from pydantic import BaseModel
from fastapi import UploadFile
from datetime import datetime

# Admin
class admin(BaseModel):
    id: int
    name: str
    program: str
    password: str
    soft_del: bool

class admincreate(admin):
    pass

class adminget(admin):
    id: int

    class config:
        from_attributes = True

# Teacher
class teacher(BaseModel):
    name: str
    program: str
    password : str
    activated_by: int

class teachercreate(teacher):
    pass

class teacherget(teacher):
    id: int

    class config:
        from_attributes = True

# Subject
class subject(BaseModel):
    id: int
    name: str
    taught_by: int

class subjectcreate(subject):
    pass

class subjectget(subject):
    id: int

    class config:
        from_attributes = True

# Student
class student(BaseModel):
    name: str
    roll_no: int
    phone : str
    program: str
    password: str

class studentcreate(student):
    pass

class studentget(student):
    id: int

    class config:
        from_attributes = True

# Summarizer
class summarizer(BaseModel):
    index: int
    student_id: int
    subject_id: int
    summary_str: str
    plagarism_score: float
    marks_scored: int
    file_path: str
    submitted_at: datetime
    reviewed: bool

class summarizercreate(summarizer):
    pass

class summarizerget(summarizer):
    index: int

    class config:
        from_attributes = True

# Summary Upload (with UploadFile)
class summaryupload(BaseModel):
    index: int
    student_id: int
    subject_id: int
    summary_text: str
    plagarism_score: float
    marks_scored: int
    file: UploadFile

# Login
class loginin(BaseModel):
    id: int
    password: str

    class config:
        from_attributes = True
# Register admin
class registeradmin(BaseModel):
    id: int
    name: str
    program: str
    password: str
    soft_del: bool
