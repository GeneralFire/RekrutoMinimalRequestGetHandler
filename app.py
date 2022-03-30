from flask_restful import Api
from flask import Flask

from rekruto_routine import Rekruto

def create_app(test=False):
    app = Flask(__name__)
    return app

def init_app(app):
    api = Api(app)
    api.add_resource(Rekruto, "/")

if __name__ == "__main__":
    app = create_app()
    init_app(app)
    app.run(host="0.0.0.0", threaded=True, debug=True)
