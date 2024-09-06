from flask_restx import Resource
from swagger_docs_api.schemas.objects_classes import namespace, delete_schema, model_get_by_id, update_schema
from core.base_crud import put, delete, get_by_id


@namespace.route('/<int:record_id>')
class GettingRecord(Resource):
    '''Чтение, обновление и удаление отдельно указываемой записи'''
    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_with(model_get_by_id)
    def get(self, record_id):
        '''Получение записи по ID'''
        return get_by_id(record_id)


    @namespace.response(204, 'Выбранная запись была успешно удалена')
    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_with(delete_schema)
    def delete(self, record_id):
        '''Удаление записи'''
        return delete(record_id)

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(update_schema)
    @namespace.marshal_with(update_schema)
    def put(self, record_id):
        '''Обновление записи'''
        return put(record_id)
