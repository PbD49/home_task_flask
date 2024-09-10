from flask.views import MethodView
from core.base_crud import get, post, put, delete, get_by_id


class BlogApiView(MethodView):
    def get(self, record_id=None):
        '''Получение записей'''
        if record_id:
            return get_by_id(record_id)
        else:
            return get()

    def post(self, owner_id):
        '''Создание записи'''
        return post(owner_id)

    def put(self, record_id):
        '''Обновление'''
        return put(record_id)

    def delete(self, record_id):
        '''Удаление'''
        return delete(record_id)
