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
        errors_data = cal.get("errors")
        main_data = {k: v for k, v in cal.items() if k != "errors"}

        biocal = BioCal(**main_data)
        biocal.errors = Errors(**errors_data)

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

def query_values():
    output = []
    session = SessionLocal()
    results = session.query(Errors).join(BioCal).filter(BioCal.result == "Pass").all()
    for result in results:
        temp = [result.wl1, result.wl2, result.wl3, result.wl4, result.wl5, result.abs1, result.abs2, result.abs3, result.abs4, result.abs5]
        output.append(temp)
    return output

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