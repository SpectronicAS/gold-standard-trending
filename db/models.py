from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from db.db import Base

class BioCal(Base):
    __tablename__ = "biocal"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
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
    result = Column(String, nullable=False)
    errors = relationship("Errors", back_populates="biocal", uselist=False)

class Errors(Base):
    __tablename__ = "errors"
    id = Column(Integer, primary_key=True)
    cal_id = Column(Integer, ForeignKey("biocal.id"), unique=True)
    
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

    biocal = relationship("BioCal", back_populates="errors")


def return_columns(table: BioCal):
    return table.__table__.columns.keys()
        