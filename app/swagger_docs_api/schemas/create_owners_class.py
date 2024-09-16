from flask_restx import fields
from app.swagger_docs_api.schemas.base_class import BaseSchema


class CreateOwnersSchema(BaseSchema):
    def __init__(self, name_space):
        super().__init__(name_space)

    def create_model(self):
        return self.name_space.model('create_owners', {
            'username': fields.String(
                required=True,
                description='Имя'
            ),
            'email': fields.String(
                required=True,
                description='Email'
            ),
            'password': fields.String(
                required=True,
                description='Пароль'
            )
        })
