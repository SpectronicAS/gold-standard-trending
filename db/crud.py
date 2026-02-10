from db import SessionLocal
from models import BioCal

def add_cal(values: dict):
    session = SessionLocal()
    data = values.keys()
    try:
        biocal = BioCal(
            wl1=data["wl1"],
            wl2=data["wl2"],
            wl3=data["wl3"],
            wl4=data["wl4"],
            wl5=data["wl5"], 
            abs1=data["abs1"], 
            abs2=data["abs2"], 
            abs3=data["abs3"],
            abs4=data["abs4"],
            abs5=data["abs5"],
            wl1var=data["wl1var"],
            wl2var=data["wl2var"],
            wl3var=data["wl3var"],
            wl4var=data["wl4var"],
            wl5var=data["wl5var"],
            abs1var=data["abs1var"], 
            abs2var=data["abs2var"],
            abs3var=data["abs3var"],
            abs4var=data["abs4var"],
            abs5var=data["abs5var"]
            )
        session.add(biocal)
        session.commit()
    finally:
        session.close()

def edit_cal(id, values: dict):
    session = SessionLocal()
    record = session.get(BioCal, id)
    try:
        if not record:
            raise ValueError("Record not Found")
    finally:
        add_cal(values)


def query_cals():
    session = SessionLocal()
    try:
        records = session.get(BioCal)
        return records
    finally:
        session.close()

