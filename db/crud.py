from db.db import SessionLocal
from db.models import BioCal, Errors


def update_values(instance, data : dict, exclude=("id",)):
    for column in instance.__table__.columns:
        name = column.name
        if name in exclude:
            continue
        if name in data:
            setattr(instance, name, data[name])

    

def add_cal(cal: dict):
    session = SessionLocal()
    try:
        biocal = BioCal(**cal)
        session.add(biocal)
        session.commit()
    finally:
        session.close()

    

def edit_cal(id, values: dict):
    session = SessionLocal()
    try:
        record = session.get(BioCal, id)
        if not record:
            return False
        update_values(record, values)
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

def query_data():
    session = SessionLocal()
    return session.query(BioCal.id, BioCal.created_at, BioCal.result).order_by(BioCal.created_at.desc()).all()

def query_values(id):
    session = SessionLocal()
    return session.query(
        BioCal.id, 
        BioCal.abs1, 
        BioCal.abs2, 
        BioCal.abs3, 
        BioCal.abs4, 
        BioCal.abs5,
        BioCal.wl1,
        BioCal.wl2,
        BioCal.wl3,
        BioCal.wl4,
        BioCal.wl5
        ).order_by(BioCal.created_at.desc()).where(BioCal.result == "Pass")

def delete_cal(id) -> bool:
    session = SessionLocal()
    try:
        record = session.get(BioCal, id)
        if not record:
            return False
        session.delete(record)
        session.commit()
    finally:
        session.close()

def get_errors(id):
    session = SessionLocal()
    data = session.query(BioCal.errors).where(BioCal.id == id)
    return data