from db.db import SessionLocal
from db.models import BioCal
from logic.calcert import Calcert
from dataclasses import asdict


def update_values(instance, data : dict, exclude=("id",)):
    for column in instance.__table__.columns:
        name = column.name
        if name in exclude:
            continue
        if name in data:
            setattr(instance, name, data[name])

    

def add_cal(cal: Calcert):
    session = SessionLocal()
    try:
        db_obj = BioCal(**asdict(cal))
        session.add(db_obj)
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
