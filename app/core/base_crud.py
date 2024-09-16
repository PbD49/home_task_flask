from app.db.postgres_db.queries_db import get_records_all, create_records, edit_record_id, delete_record, get_record_id
from flask import request


def list_records():
    '''Получение всех записей'''
    entities = [
        {
            'id': entity['id'],
            'heading': entity['heading'],
            'description': entity['description'],
            'date_add': str(entity['date_add']),
            'date_update': str(entity['date_update']),
            'owner_id': entity['owner_id']
        } for entity in get_records_all()
    ]
    return {
        'total_records': len(entities),
        'records': entities
    }


def create_record(owner_id):
    '''Создание записи'''
    data = request.get_json()
    return create_records(data, owner_id), 201


def edit_record(record_id):
    '''Обновление'''
    data = request.get_json()
    entity = edit_record_id(record_id, data)
    if entity:
        return {
            'id': entity.id,
            'heading': entity.heading,
            'description': entity.description,
            'date_add': str(entity.date_add),
            'date_update': str(entity.date_update),
            'owner_id': entity.owner.id
        }
    else:
        return


def delete_records(record_id):
    '''Удаление'''
    delete = delete_record(record_id)
    return delete, 204


def get_by_id(record_id):
    '''Получение по ID'''
    entity = get_record_id(record_id)
    if entity:
        return {
            'records': {
                'id': entity.id,
                'heading': entity.heading,
                'description': entity.description,
                'date_add': str(entity.date_add),
                'date_update': str(entity.date_update),
                'owner_id': entity.owner.id
            }
        }
    else:
        return {'message': 'Record not found'}, 404
