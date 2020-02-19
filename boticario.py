"""This file is the main module which contains the app, where all the good
stuff happens. You will always want to point your applications like Gunicorn
to this file, which will pick up the app to run their servers.
"""
from flask_migrate import Migrate, upgrade
from app import create_app, db
from decouple import config

env_config = config("ENV", cast=str, default="develop")

app = create_app(env_config)
migrate = Migrate(app, db)


@app.cli.command()
def deploy():
    upgrade()
