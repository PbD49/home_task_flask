from flask import Blueprint
from website.views import BlogApiView


crud_bp = Blueprint('crud_bp', __name__, url_prefix='/api/v1')
crud_bp.add_url_rule('/records', defaults={'record_id': None}, view_func=BlogApiView.as_view('get_records'), methods=['GET'])
crud_bp.add_url_rule('/records/create/<int:owner_id>', view_func=BlogApiView.as_view('create_record'), methods=['POST'])
crud_bp.add_url_rule('/records/<int:record_id>', view_func=BlogApiView.as_view('get_record'), methods=['GET'])
crud_bp.add_url_rule('/records/<int:record_id>', view_func=BlogApiView.as_view('update_record'), methods=['PUT'])
crud_bp.add_url_rule('/records/<int:record_id>', view_func=BlogApiView.as_view('delete_record'), methods=['DELETE'])
