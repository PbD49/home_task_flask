from app.swagger_docs_api.schemas.base_class import BaseSchema, namespace
from app.swagger_docs_api.schemas.get_by_id_class import GetByIdSchema
from app.swagger_docs_api.schemas.create_update_delete_class import CreateAndUpdateDeleteSchema
from app.swagger_docs_api.schemas.create_owners_class import CreateOwnersSchema

base_schema = BaseSchema(namespace)
get_by_id_schema = GetByIdSchema(namespace)
create_update_delete_schema = CreateAndUpdateDeleteSchema(namespace)
create_owners_schema = CreateOwnersSchema(namespace)


model_group = base_schema.group_model()
model_get_by_id = get_by_id_schema.group_model()
create_schema = create_update_delete_schema.create_model()
update_schema = create_update_delete_schema.update_model()
delete_schema = create_update_delete_schema.delete_model()
create_owners = create_owners_schema.create_model()
