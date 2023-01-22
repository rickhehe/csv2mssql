from sqlalchemy import Column, Integer, String, Date
from base import Base

class DimHolidayNZ(Base):

    __tablename__ = 'dimHolidayNZ'

    id = Column(Integer, primary_key=True)
    name = Column(String(55))
    dateKey = Column(Integer)

class DimDept(Base):

    __tablename__ = 'dimDept'

    id = Column(Integer, primary_key=True)
    name = Column(String(55))
    groupName = Column(String(55))

