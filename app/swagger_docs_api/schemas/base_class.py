from flask_restx import fields, Namespace


namespace = Namespace('website',
                      'Примеры API запросов')


class BaseSchema:
    def __init__(self, name_space):
        self.name_space = name_space

    def base_model(self):
        return self.name_space.model('get', {
            'id': fields.Integer(
                readonly=True,
                description='Идентификатор'
            ),
            'heading': fields.String(
                required=True,
                description='Название'
            ),
            'description': fields.String(
                required=True,
                description='Описание'
            ),
            'date_add': fields.String(
                required=True,
                description='Дата добавления'
            ),
            'date_update': fields.String(
                required=True,
                description='Дата обновления'
            ),
            'owner_id': fields.String(
                required=True,
                description='Идентификатор владельца'
            )
        })

    def group_model(self):
        base_model = self.base_model()
        return self.name_space.model('group', {
            'total_records': fields.Integer(
                description='Общее количество',
            ),
            'records': fields.Nested(
                base_model,
                description='Записи',
                as_list=True
            ),
        })
