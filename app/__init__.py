from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
        app.config['SQLALCHEMY_ECHO'] = True

    else:
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")
        app.config['SQLALCHEMY_ECHO'] = True

    # import models here
    from app.models.planet import Planet

    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints here
    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    return app
