from flask import Flask

from app.db.postgres_db.engine_postgres import create_tables
from app.swagger_docs_api.config import swagger_bp
from app.website.router_bp import crud_bp


app = Flask(__name__)


blueprints = [crud_bp, swagger_bp]


for blueprint in blueprints:
    app.register_blueprint(blueprint)


app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False


if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
