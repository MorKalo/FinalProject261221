from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
#from sqlalchemy.orm import relationship
from Db_config import Base

class Administrators(Base):
    __tablename__ = 'administrators'

    # static fields *********לשים nullable איפה שצריך***********  nullable=False
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    first_name= Column(String())
    last_name=Column(String())
    user_id=Column(BigInteger(), unique=True)


    def __repr__(self):
        return f'\n<id={self.id} first_name={self.first_name} last_name={self.last_name} user_id={self.user_id} >'

    def __str__(self):
        return f'\n<id={self.id} first_name={self.first_name} last_name={self.last_name} user_id={self.user_id} >'

