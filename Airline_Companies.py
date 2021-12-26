from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
#from sqlalchemy.orm import relationship
from Db_config import Base

class Airline_Companies(Base):
    __tablename__ = 'airline_companies'

    # static fields *********לשים nullable איפה שצריך***********  nullable=False
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name= Column(String(), unique=True)
    country_id=Column(Integer())
    user_id=Column(BigInteger(), unique=True)


    def __repr__(self):
        return f'\n<id={self.id} name={self.name} country_id={self.country_id} user_id={self.user_id} >'

    def __str__(self):
        return f'\n<id={self.id} name={self.name} country_id={self.country_id} user_id={self.user_id} >'


