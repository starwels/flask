# Flask Imports
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from config import config_dict


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_key='local'):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_key])
    config_dict[config_key].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.api import api as api_blueprint

    app.register_blueprint(api_blueprint)

    return app
