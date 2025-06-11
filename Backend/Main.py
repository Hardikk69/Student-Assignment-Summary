from Schemas import *
from Services import *
from Models import *
from Models import *
from Database import  get_db
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, Form, UploadFile,File

##################
"""""""APIS"""""""
##################
app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return {"message": "Hello world!"}


@app.post("/login")
def logIn(login_data: loginin, db: Session = Depends(get_db)):
    return login(login_data, db)

@app.post("/create-admin/")
def createadmin(admin:admincreate,db:Session=Depends(get_db)):
    return create_admin(admin,db)

@app.get("/get-admin/")
def getadmin(db:Session=Depends(get_db)):
    return get_admin(db)

@app.post("/create-teacher/")
def createteacher(teacher:teachercreate,db:Session=Depends(get_db)):
    return create_teacher(teacher,db)

@app.get("/get-teacher/")
def getteacher(db:Session=Depends(get_db)):
    return get_teacher(db)

@app.put("/update-teacher/{id}")
def updateteacher(teacher:teachercreate,id:int,db:Session=Depends(get_db)):
    return update_teacher(teacher,id,db)

@app.delete("/delete-teacher/{id}")
def deleteteacher(id:int,db:Session=Depends(get_db)):
    return delete_teacher(id,db)

@app.post("/create-student/")
def createstudent(student:studentcreate,db:Session=Depends(get_db)):
    return create_student(student,db)

@app.get("/get-student/")
def getstudent(db:Session=Depends(get_db)):
    return get_student(db)

@app.put("/update-student/{id}")
def updatestudent(subject: studentcreate,id: int,db: Session = Depends(get_db)):
    return update_student(subject, id, db)

@app.delete("/delete-student/{id}")
def deletestudent(id:int,db:Session=Depends(get_db)):
    return delete_student(id,db)

@app.post("/create-subject/")
def createsubject(subject:subjectcreate,db:Session=Depends(get_db)):
    return create_subject(subject,db)

@app.get("/get-subject/")
def getsubject(db:Session=Depends(get_db)):
    return get_subject(db)

@app.put("/update-subject/{id}")
def updatesubject(subject:subjectcreate,subject_id:int,db:Session=Depends(get_db)):
    return update_subject(subject,subject_id,db)

# @app.post("/register/")
# async def Register(registerin:Register_admin_In,db:db_dependency):
#     admin_cred = Models.Admin_table(
#         Id=registerin.id,
#         Name=registerin.name,
#         program=registerin.program,
#         Password=registerin.password,
#         Soft_del=registerin.soft_del,
#     )    
#     db.add(admin_cred)
#     db.commit()
#     db.refresh(admin_cred)
#     return {"message:":"Added succesfully"}

@app.post("/upload-pdf/")
async def upload_pdf(
    index: int = Form(...),
    student_id: int = Form(...),
    subject_id: int = Form(...),
    summary_text: str = Form(...),
    plagarism_score: float = Form(...),
    marks_scored: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    file_bytes = await file.read()

    summary = Summarizer(
        Index=index,
        Student_id=student_id,
        Subject_id=subject_id,
        Summary_text=summary_text,
        Plagarism_score=plagarism_score,
        Marks_scored=marks_scored,
        file_name=file.filename,
        file_data=file_bytes,
        Submitted_at=datetime.now().time(),
        Reviewed=False
    )

    db.add(summary)
    db.commit()
    db.refresh(summary)

    return {"message": "PDF uploaded and stored in database successfully"}