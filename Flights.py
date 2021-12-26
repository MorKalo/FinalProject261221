from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
#from sqlalchemy.orm import relationship
from Db_config import Base

class Flights(Base):
    __tablename__ = 'flights'

    # static fields *********לשים nullable איפה שצריך***********  nullable=False
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    Airline_Company_Id= Column(BigInteger())
    Origin_Country_id= Column(Integer())
    Destination_Country_id=Column(Integer())
    Departure_Time=Column(DateTime())
    Landing_Time=Column(DateTime())
    Remaining_Tickets=Column(Integer())


    def __repr__(self):
        return f'\n<id={self.id} Airline_Company_Id={self.Airline_Company_Id} Origin_Country_id{self.Origin_Country_id}\
         Destination_Country_id = {self.Destination_Country_id} Departure_Time={self.Departure_Time}\
          Landing_Time={self.Landing_Time} Remaining_Tickets={self.Remaining_Tickets}>'

    def __str__(self):
        return f'\n<id={self.id} Airline_Company_Id={self.Airline_Company_Id} Origin_Country_id{self.Origin_Country_id}\
         Destination_Country_id = {self.Destination_Country_id} Departure_Time={self.Departure_Time}\
          Landing_Time={self.Landing_Time} Remaining_Tickets={self.Remaining_Tickets}>'


