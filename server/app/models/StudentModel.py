from sqlalchemy import Column, Integer,String, Boolean,Date
from ..db import Base
from ..models import UserModel

from .BaseModel import BaseModel


class StudentModel(BaseModel,Base):
    __tablename__ = 'student'
    student_id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    fname_kh = Column(String(50), nullable=False)
    lname_kh = Column(String(50), nullable=False)
    fname_en = Column(String(50), nullable=False)
    lname_en = Column(String(50), nullable=False)
    gender   = Column(String(10), nullable=False)
    dob      = Column(Date, nullable=True)
    pob = Column(String(255), nullable=False)
    current_addr = Column(String(255), nullable=False)
    region   = Column(String(50), nullable=False)
    grade_id = Column(Integer, nullable=True) 
    o_grade_id = Column(Integer, nullable=True) 
    roll = Column(String(50), nullable=False)
    transfer = Column(String(50), nullable=False)
    number = Column(String(255), nullable=False)
    mother_name = Column(String(50), nullable=False)
    father_name = Column(String(50), nullable=False)
    mother_job = Column(String(50), nullable=False)
    father_job = Column(String(50), nullable=False)
    contact = Column(String(50), nullable=False)
    mobile = Column(String(50), nullable=False)
    email  = Column(String(50), nullable=False)
    username  = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    national_id = Column(Integer, nullable=False)
    types = Column(String(50), nullable=False)
    family_types = Column(String(50), nullable=False)
    scholarship = Column(String(50), nullable=False)
    vaccine = Column(Boolean)
    vaccine_id = Column(Integer, nullable=False)
    admission_date = Column(Date, nullable=True)
    img = Column(String(50), nullable=False)
    disc = Column(String(50), nullable=False)
    status = Column(Boolean)