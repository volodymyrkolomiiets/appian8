import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    environment_configuration = os.environ["CONFIGURATION_SETUP"]
    app.config.from_object(environment_configuration)

    db.init_app(app)
    with app.app_context():
        from .product_api import product_blueprint
        app.register_blueprint(product_blueprint)
        return app

