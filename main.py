from flask import Flask
from swagger_docs_api.config import swagger_bp
from website.router_bp import crud_bp


app = Flask(__name__)


blueprints = [crud_bp, swagger_bp]


for blueprint in blueprints:
    app.register_blueprint(blueprint)


app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
