import time
from datetime import datetime
from sqlalchemy.orm import joinedload, declarative_base
from db.postgres_db.engine_postgres import session
from db.redis_db.redis_db import RedisDB
from db.postgres_db.model import Owners, Website

Base = declarative_base()


def get_records_all():
    records = session.query(Website) \
                     .options(joinedload(Website.owner)) \
                     .order_by(Website.date_add.asc()) \
                     .all()

    return [
        {
            "id": record.id,
            "heading": record.heading,
            "description": record.description,
            "date_add": str(record.date_add),
            "date_update": str(record.date_update),
            "owner_id": record.owner.id
        } for record in records]



def create_records(data, owner_id):
    owner = session.query(Owners).filter_by(id=owner_id).first()
    if not owner:
        return {"error": "Owner not found"}, 400

    # Создаем новый объект сайта
    new_record = Website(
        heading=data['heading'],
        description=data['description'],
        date_add=datetime.now(),
        date_update=datetime.now(),
        owner_id=owner.id
    )
    session.add(new_record)
    session.commit()

    return {
        "id": new_record.id,
        "heading": new_record.heading,
        "description": new_record.description,
        "owner_id": new_record.owner_id,
        "date_add": new_record.date_add,
        "date_update": new_record.date_update
    }


def get_record_id(record_id):
    record = session.query(Website) \
                    .options(joinedload(Website.owner)) \
                    .filter(Website.id == record_id) \
                    .one_or_none()
    return record


def delete_record(record_id: int):
    record = session.query(Website).get(record_id)
    if record:
        session.delete(record)
        session.commit()
        return {"message": f"Record with ID {record_id} has been deleted."}
    else:
        return {"message": f"Record with ID {record_id} not found."}, 404


def edit_record_id(record_id, data):
    record = session.query(Website) \
                    .options(joinedload(Website.owner)) \
                    .filter(Website.id == record_id) \
                    .one_or_none()
    if record:
        record.heading = data.get('heading', record.heading)
        record.description = data.get('description', record.description)
        if 'owner_id' in data:
            record.owner.id = data['owner_id']
        session.commit()
        return record
    else:
        return


def save_user(user):
    session.add(user)
    session.commit()
    update_user_cache(user)
    session.close()

def update_user_cache(user):
    redis_db = RedisDB()
    redis_db.update_user_cache(user)

def update_user_cache_periodically():
    redis_db = RedisDB()
    while True:
        users = session.query(Owners).all()
        session.close()
        for user in users:
            redis_db.update_user_cache(user)
        time.sleep(2)
