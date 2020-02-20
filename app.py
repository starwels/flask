from flask_migrate import Migrate
from decouple import config
from flask import Flask
from config import config_dict
from flask_sqlalchemy import SQLAlchemy

env_config = config("ENV", cast=str, default="develop")
db = SQLAlchemy()
app = Flask(__name__)
migrate = Migrate(app, db)
app.config.from_object(config_dict['local'])
config_dict['local'].init_app(app)

db.init_app(app)
migrate.init_app(app, db)

from api import api as api_blueprint

app.register_blueprint(api_blueprint)
