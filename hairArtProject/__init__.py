#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "users.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "uniquepassword"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from hairArtProject.views.auth import auth
    from hairArtProject.views.services import services
    from hairArtProject.views.appointments import appointments

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(services, url_prefix="/")
    app.register_blueprint(appointments, url_prefix="/")

    from hairArtProject.models import Customer

    with app.app_context():
        db.create_all()

    return app


def create_database():
    """creates database instances"""
    if not path.exists("hairArtProject/" + DB_NAME):
        db.create_all(app=app)
