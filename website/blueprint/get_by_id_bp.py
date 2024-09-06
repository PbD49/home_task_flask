from flask import Blueprint
from website.views import BlogApiViewGetById


get_by_id_bp = Blueprint('get_by_id_record', __name__)
get_by_id_bp.add_url_rule('/api/v1/get_by_id_record/<int:record_id>', view_func=BlogApiViewGetById.as_view('get_by_id_record'))
