from db import SessionLocal
from models import BioCal

def add_cal(wl1, wl2, wl3, wl4, wl5, abs1, abs2, abs3, abs4, abs5, wl1var, wl2var, wl3var, wl4var, wl5var, abs1var, abs2var, abs3var, abs4var, abs5var):
    session = SessionLocal()
    try:
        biocal = BioCal(
            wl1=wl1,
            wl2=wl2,
            wl3=wl3, 
            wl4=wl4, 
            wl5=wl5, 
            abs1=abs1, 
            abs2=abs2, 
            abs3=abs3, 
            abs4=abs4, 
            abs5=abs5,
            wl1var=wl1var,
            wl2var=wl2var, 
            wl3var=wl3var, 
            wl4var=wl4var, 
            wl5var=wl5var, 
            abs1var=abs1var, 
            abs2var=abs2var, 
            abs3var=abs3var, 
            abs4var=abs4var, 
            abs5var=abs5var
            )
        session.add(biocal)
        session.commit()
    finally:
        session.close()

def query_cals():
    session = SessionLocal()
    try:
        records = session.get(BioCal)
        return records
    finally:
        session.close()

