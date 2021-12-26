from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
#from sqlalchemy.orm import relationship
from Db_config import Base

class Users(Base):
    __tablename__ = 'users'

    # static fields *********לשים nullable איפה שצריך***********  nullable=False
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    username= Column(String(), unique=True)
    password=Column(String())
    email=Column(String(), unique=True)
    user_role=Column(Integer())


    def __repr__(self):
        return f'\n<id={self.id} username={self.username} password={self.password} email={self.email}\
         user_role={self.user_role} >'

    def __str__(self):
        return f'\n<id={self.id} username={self.username} password={self.password} email={self.email}\
         user_role={self.user_role} >'

