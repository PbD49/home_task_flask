from flask_restx import Resource
from swagger_docs_api.schemas.objects_classes import namespace, model_group
from core.base_crud import get


@namespace.route('/get_records')
class GettingAllRecords(Resource):
    '''Получение всех запипей'''
    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_list_with(model_group)
    def get(self):
        '''Получение всех записей'''
        return get()
