from db import SessionLocal
from models import BioCal


def update_values(instance, data : dict, exclude=("id",)):
    for column in instance.__table__.columns:
        name = column.name
        if name in exclude:
            continue
        if name in data:
            setattr(instance, name, data[name])

    

def add_cal(values: dict):
    session = SessionLocal()
    try:
        record = BioCal()
        update_values(record, values)
        session.add(record)
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
