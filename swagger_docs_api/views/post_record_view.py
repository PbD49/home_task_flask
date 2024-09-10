from flask_restx import Resource
from http import HTTPStatus
from swagger_docs_api.schemas.objects_classes import namespace, create_schema
from core.base_crud import create_record


@namespace.route('/<int:owner_id>')
class CreateRecord(Resource):
    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(create_schema)
    @namespace.marshal_with(create_schema, code=HTTPStatus.CREATED)
    def post(self, owner_id):
        '''Создание записи'''
        return create_record(owner_id)
