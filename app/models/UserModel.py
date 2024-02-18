
from sqlalchemy import Column, Integer,String
from ..db import Base

from .BaseModel import BaseModel

class UserModel(BaseModel,Base):
    __tablename__ = 'users'

    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    __username = Column("username",String(80), unique=True, nullable=False)
    email = Column(String(120), nullable=False)
    __password = Column("password",String(120), unique=True, nullable=False)  

    def __init__(self,schema={ }):
        super().__init__()

        for key, value in schema.items():
            if(hasattr(self,key)):
                setattr(self,key,value)

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self,username):
        self.__username = username

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        self.__password = password

