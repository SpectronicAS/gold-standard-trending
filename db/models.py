from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class BioCal(Base):
    __tablename__ = "biocal"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.timezone.utc)
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
    wl1var = Column(Float, nullable=False)
    wl2var = Column(Float, nullable=False)
    wl3var = Column(Float, nullable=False)
    wl4var = Column(Float, nullable=False)
    wl5var = Column(Float, nullable=False)
    abs1var = Column(Float, nullable=False)
    abs2var = Column(Float, nullable=False)
    abs3var = Column(Float, nullable=False)
    abs4var = Column(Float, nullable=False)
    abs5var = Column(Float, nullable=False)