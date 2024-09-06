from flask_restx import fields
from .base_class import BaseSchema


class GetByIdSchema(BaseSchema):
    def base_model(self):
        base_model = super().base_model()
        return self.name_space.model('get', {
            **base_model
        })

    def group_model(self):
        base_model = self.base_model()
        return self.name_space.model('group', {
            'records': fields.Nested(
                base_model,
                description='Записи',
                as_list=True
            ),
        })
