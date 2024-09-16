from flask_restx import fields
from .base_class import BaseSchema


class CreateAndUpdateDeleteSchema(BaseSchema):
    def __init__(self, name_space):
        super().__init__(name_space)

    def create_model(self):
        return self.name_space.model('create', {
            'heading': fields.String(
                required=True,
                description='Название'
            ),
            'description': fields.String(
                required=True,
                description='Описание'
            ),
        })

    def update_model(self):
        return self.name_space.model('update', {
            'heading': fields.String(
                required=True,
                description='Название'
            ),
            'description': fields.String(
                required=True,
                description='Описание'
            )
        })

    def delete_model(self):
        return self.name_space.model('delete', {
    'id': fields.String(
        required=True,
        description='Идентификатор'
    )
})
