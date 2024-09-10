from flask.views import MethodView
from core.base_crud import list_records, create_record, edit_record_id, delete_records, get_by_id


class BlogApiView(MethodView):
    def get(self, record_id=None):
        '''Получение записей'''
        if record_id:
            return get_by_id(record_id)
        else:
            return list_records()

    def post(self, owner_id):
        '''Создание записи'''
        return create_record(owner_id)

    def put(self, record_id):
        '''Обновление'''
        return edit_record_id(record_id)

    def delete(self, record_id):
        '''Удаление'''
        return delete_records(record_id)
