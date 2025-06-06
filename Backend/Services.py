from fastapi import HTTPException
from Schemas import *
from Models import *
from sqlalchemy.orm import Session

def login(login_data: Login, db: Session):
    user_id = login_data.id
    password = login_data.password

    if user_id >= 22000:
        student = db.query(Student).filter(Student.id == user_id).first()
        if student and student.password == password:
            return {"message": f"Welcome, {student.name}", "role": "student"}

    elif user_id >= 10000 & user_id<=20000:
        teacher = db.query(Teacher).filter(Teacher.id == user_id).first()
        if teacher and teacher.password == password:
            return {"message": f"Welcome, {teacher.name}", "role": "teacher"}

    else:
        admin = db.query(Admin_table).filter(Admin_table.id == user_id).first()
        if admin and admin.password == password:
            return {"message": f"Welcome, {admin.name}", "role": "admin"}

    raise HTTPException(status_code=401, detail="Invalid credentials")

def create_admin(data: admincreate, db: Session):
    admin_instance = Admin_table(
        id=data.id,
        name=data.name,
        program=data.program,
        password=data.password,
        soft_del=data.soft_del
    )
    db.add(admin_instance)
    db.commit()
    db.refresh(admin_instance)
    return admin_instance

def get_admin(db:Session):
    return db.query(Admin_table).where(Admin_table.soft_del == False).all()

def create_teacher(data:teachercreate,db:Session):
    teacher_instance = Teacher(
        id=data.id,
        name=data.name,
        program=data.program,
        password=data.password,
        activated_by=data.activated_by,
        soft_del=data.soft_del
    )
    db.add(teacher_instance)
    db.commit()
    db.refresh(teacher_instance)
    return teacher_instance

def get_teacher(db:Session):
    return db.query(Teacher).where(Teacher.soft_del == False).all()

def create_student(data:studentcreate,db:Session):
    student_instance = Student(
        id=data.id,
        name=data.name,
        roll_no=data.roll_no,
        phone=data.phone,
        program=data.program,
        password=data.password,
        soft_del=data.soft_del
    )
    db.add(student_instance)
    db.commit()
    db.refresh(student_instance)
    return student_instance

def get_student(db:Session):
    return db.query(Student).where(Student.soft_del == False).all()

def create_subject(data:subjectcreate,db:Session):
    subject_instance = Subject(
        id=data.id,
        name=data.name,
        taught_by=data.taught_by
    )
    db.add(subject_instance)
    db.commit()
    db.refresh(subject_instance)
    return subject_instance

def get_subject(db:Session):
    return db.query(Subject).all()