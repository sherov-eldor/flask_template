from flask import Flask
from src.routes.base import base_route

def create_app():
    app = Flask(__name__)

    app.register_blueprint(base_route)

    return app