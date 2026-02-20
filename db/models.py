from sqlalchemy import Column, Integer, Float, DateTime, Boolean, String
from datetime import datetime
from db.db import Base

class BioCal(Base):
    __tablename__ = "biocal"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.astimezone)
    wl1 = Column(Float, nullable=False)
    wl2 = Column(Float, nullable=False)
    wl3 = Column(Float, nullable=False)
    wl4 = Column(Float, nullable=False)
    wl5 = Column(Float, nullable=False)
    abs1 = Column(Float, nullable=False)
    abs2 = Column(Float, nullable=False)
    abs3 = Column(Float, nullable=False)
    abs4 = Column(Float, nullable=False)
    abs5 = Column(Float, nullable=False)
    setname = Column(String, nullable=False)
    result = Column(Boolean, nullable=False)


def return_columns(table: BioCal):
    return table.__table__.columns.keys()
        