from flask import Blueprint
from website.views import BlogApiViewDelete


delete_bp = Blueprint('delete_record', __name__)
delete_bp.add_url_rule('/api/v1/delete_record/<int:record_id>', view_func=BlogApiViewDelete.as_view('delete_record'))
