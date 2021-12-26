from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
#from sqlalchemy.orm import relationship
from Db_config import Base

class Tickets(Base):
    __tablename__ = 'tickets'

    # static fields *********לשים nullable איפה שצריך***********  nullable=False
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    flght_id= Column(BigInteger())
    customer_id=Column(BigInteger()) #לשים לב שהחיבור של 2 השדות הוא יוניקי


    def __repr__(self):
        return f'\n<id={self.id} flght_id={self.flght_id} customer_id{self.customer_id} >'

    def __str__(self):
        return f'\n<id={self.id} flght_id={self.flght_id} customer_id{self.customer_id} >'


