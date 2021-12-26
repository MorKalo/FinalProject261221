from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
#from sqlalchemy.orm import relationship
from Db_config import Base

class Airline_Companies(Base):
    __tablename__ = 'airline_companies'

    # static fields *********לשים nullable איפה שצריך***********  nullable=False
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    first_name= Column(String())
    last_name= Column(String())
    address=Column(String())
    phone_number=Column(String(), unique=True)
    cradit_card_no=Column(String(), unique=True)
    user_id=Column(BigInteger(), unique=True)


    def __repr__(self):
        return f'\n<id={self.id} first_name={self.first_name} last_name={self.last_name} address={self.address}\
         phone_number={self.phone_number} cradit_card_no={self.cradit_card_no} user_id={self.user_id}>'

    def __str__(self):
        return f'\n<id={self.id} first_name={self.first_name} last_name={self.last_name} address={self.address}\
         phone_number={self.phone_number} cradit_card_no={self.cradit_card_no} user_id={self.user_id}>'

