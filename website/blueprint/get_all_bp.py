from flask import Blueprint
from website.views import BlogApiViewList


get_bp = Blueprint('list_records', __name__)
get_bp.add_url_rule('/api/v1/list_records', view_func=BlogApiViewList.as_view('list_records'))
