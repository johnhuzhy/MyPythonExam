# project/__init__.py
from flask import Flask


def create_app():
    """init_app"""
    from . import models, routes, services
    app = Flask(__name__)
    models.init(app)
    routes.init(app)
    services.init(app)
    return app
