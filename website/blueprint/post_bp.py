from flask import Blueprint
from website.views import BlogApiViewCreate


post_bp = Blueprint('create_record', __name__)
post_bp.add_url_rule('/api/v1/create_record/<int:owner_id>', view_func=BlogApiViewCreate.as_view('create_record'))
