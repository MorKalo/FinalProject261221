from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
#from sqlalchemy.orm import relationship
from Db_config import Base

class Countries(Base):
    __tablename__ = 'countries'

    # static fields *********לשים nullable איפה שצריך***********  nullable=False
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name= Column(String(), unique=True)


    def __repr__(self):
        return f'\n<id={self.id} name={self.name} >'

    def __str__(self):
        return f'\n<id={self.id} name={self.name} >'


