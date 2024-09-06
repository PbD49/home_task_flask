from flask import Blueprint
from website.views import BlogApiViewUpdate


update_bp = Blueprint('update_records', __name__)
update_bp.add_url_rule('/api/v1/update_records/<int:record_id>', view_func=BlogApiViewUpdate.as_view('update_records'))
