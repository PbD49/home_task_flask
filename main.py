from flask import Flask
from swagger_docs_api.config import swagger_bp
from website.blueprint.delete_bp import delete_bp
from website.blueprint.get_all_bp import get_bp
from website.blueprint.get_by_id_bp import get_by_id_bp
from website.blueprint.post_bp import post_bp
from website.blueprint.put_bp import update_bp


app = Flask(__name__)


blueprints = [get_bp, post_bp, update_bp, get_by_id_bp, delete_bp, swagger_bp]


for blueprint in blueprints:
    app.register_blueprint(blueprint)


app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
