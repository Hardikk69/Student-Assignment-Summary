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
        name=data.name,
        program=data.program,
        password=data.password,
        activated_by=data.activated_by,
    )
    db.add(teacher_instance)
    db.commit()
    db.refresh(teacher_instance)
    return teacher_instance

def get_teacher(db:Session):
    return db.query(Teacher).where(Teacher.soft_del == False).all()

def update_teacher(teacher:teachercreate,teacher_id:int,db:Session):
    teacher_update=db.query(Teacher).filter(Teacher.id==teacher_id).first()
    if teacher_update:
        for key,value in teacher.model_dump().items():
            setattr(teacher_update,key,value)
        db.commit()
        db.refresh(teacher_update)
        return teacher_update
    
def delete_teacher(teacher_id:int,db:Session):
    teacher_delete=db.query(Teacher).filter(Teacher.id==teacher_id).first()
    if teacher_delete:
        db.delete(teacher_delete)
        db.commit()
    return teacher_delete

def create_student(data:studentcreate,db:Session):
    student_instance = Student(
        name=data.name,
        roll_no=data.roll_no,
        phone=data.phone,
        program=data.program,
        password=data.password,
    )
    db.add(student_instance)
    db.commit()
    db.refresh(student_instance)
    return student_instance

def get_student(db:Session):
    return db.query(Student).where(Student.soft_del == False).all()

def update_student(student:studentcreate,student_id:int,db:Session):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    for key,value in student.model_dump().items():
        setattr(db_student, key, value)
    db.commit()
    db.refresh(db_student)
    return db_student
    
def delete_student(student_id:int,db:Session):
    student_delete=db.query(Student).filter(Student.id==student_id).first()
    if student_delete:
        db.delete(student_delete)
        db.commit()
    return student_delete

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

def update_subject(subject:subjectcreate,subject_id:int,db:Session):
    subject_update=db.query(Subject).filter(Subject.id==subject_id).first()
    if subject_update:
        for key,value in subject.model_dump().items():
            setattr(subject_update,key,value)
        db.commit()
        db.refresh(subject_update)
        return subject_update
    