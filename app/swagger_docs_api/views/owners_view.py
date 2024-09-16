from flask import request
from flask_restx import Resource
from app.db.postgres_db.model import Owners
from app.db.postgres_db.queries_db import save_user
from app.swagger_docs_api.schemas.objects_classes import namespace,  create_owners


@namespace.route('/create_owner')
class CreateOwners(Resource):
    @namespace.expect(create_owners)
    @namespace.marshal_list_with(create_owners)
    @namespace.response(500, 'Internal Server error')
    def post(self):
        '''Создание владельца'''
        data = request.get_json()
        new_user = Owners(
            username=data['username'],
            email=data['email']
        )
        new_user.set_password(data['password'])

        save_user(new_user)
        return new_user, 201
