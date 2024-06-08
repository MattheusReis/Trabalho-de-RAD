from flask import Flask
from settings.settings import Config
from database.database import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    return app