from flask import Blueprint
from flask_restx import Api

from .views.post_record_view import namespace as post_record
from .views.owners_view import namespace as owners
from .views.get_put_delete_record_view import namespace as get_put_delete_record
from .views.get_records_view import namespace as get_records

swagger_bp = Blueprint('swagger', __name__)


api_extension = Api(
    swagger_bp,
    title='Документация CRUD',
    version='1.0',
    description='В данной документации вы можете протестировать ручки API сайта объявлений',
    doc='/docs'
)


api_extension.add_namespace(get_put_delete_record)
api_extension.add_namespace(owners)
api_extension.add_namespace(get_records)
api_extension.add_namespace(post_record)
