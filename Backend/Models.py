from sqlalchemy import (
    Column, Integer, Boolean, ForeignKey, LargeBinary, Text, Float, Time, TIMESTAMP
)
from Database import Base
from sqlalchemy.orm import relationship

SCHEMA = "Student_assignment_system"

class Admin_table(Base):
    __tablename__ = "admin_table"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    school = Column(Text)
    password = Column(Text, nullable=False)
    soft_del = Column(Boolean, default=False)

    teachers = relationship(
        "Teacher",
        back_populates="activated_by_admin",
        cascade="all, delete",
        passive_deletes=True
    )

class Teacher(Base):
    __tablename__ = "teacher"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    school = Column(Text)
    password = Column(Text, nullable=False)
    activated_by = Column(
        Integer,
        ForeignKey(f"{SCHEMA}.admin_table.id", ondelete="CASCADE"),
        nullable=True
    )
    activated_at = Column(TIMESTAMP)

    activated_by_admin = relationship(
        "Admin_table",
        back_populates="teachers"
    )

    subjects = relationship(
        "Subject",
        back_populates="teacher",
        cascade="all, delete",
        passive_deletes=True
    )

class Subject(Base):
    __tablename__ = "subject"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    taught_by = Column(Integer,
        ForeignKey(f"{SCHEMA}.teacher.id", ondelete="CASCADE"),
        nullable=True
    )

    teacher = relationship(
        "Teacher",
        back_populates="subjects"
    )

    summaries = relationship(
        "Summarizer",
        order_by="Summarizer.index",
        back_populates="subject",
        cascade="all, delete",
        passive_deletes=True
    )

class Student(Base):
    __tablename__ = "student"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    roll_no = Column(Integer)
    phone = Column(Text, nullable=False)
    program = Column(Text)
    password = Column(Text)
    soft_del = Column(Boolean, default=False)

    summaries = relationship(
        "Summarizer",
        order_by="Summarizer.index",
        back_populates="student",
        cascade="all, delete",
        passive_deletes=True
    )

class Summarizer(Base):
    __tablename__ = "summarizer"
    __table_args__ = {"schema": SCHEMA}

    index = Column(Integer, primary_key=True)
    student_id = Column(
        Integer,
        ForeignKey(f"{SCHEMA}.student.id", ondelete="CASCADE"),
        nullable=True
    )
    subject_id = Column(
        Integer,
        ForeignKey(f"{SCHEMA}.subject.id", ondelete="CASCADE"),
        nullable=True
    )
    summary_text = Column(Text)
    plagarism_score = Column(Float)
    marks_scored = Column(Integer)
    file_name = Column(Text)
    file_data = Column(LargeBinary)
    submitted_at = Column(Time)
    reviewed = Column(Boolean, default=False)

    student = relationship(
        "Student",
        back_populates="summaries"
    )
    subject = relationship(
        "Subject",
        back_populates="summaries"
    )

class Login(Base):
    __tablename__ = "login"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    role = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    last_login = Column(TIMESTAMP)
