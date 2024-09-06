from flask.views import MethodView
from core.base_crud import get, post, put, delete, get_by_id


class BlogApiViewList(MethodView):
    def get(self):
        '''Получение всех записей'''
        return get()


class BlogApiViewCreate(MethodView):
    def post(self, owner_id):
        '''Создание записи'''
        return post(owner_id)


class BlogApiViewUpdate(MethodView):
    def put(self, record_id):
        '''Обновление'''
        return put(record_id)


class BlogApiViewDelete(MethodView):
    def delete(self, record_id):
        '''Удаление'''
        return delete(record_id)


class BlogApiViewGetById(MethodView):
    def get(self, record_id):
        '''Получение по ID'''
        return get_by_id(record_id)
