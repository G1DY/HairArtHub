#!/usr/bin/env python3
from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "users.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "uniquepassword"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from hairArtProject.views.appointments import appointments
    from hairArtProject.views.auth import auth
    from hairArtProject.views.services import services

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(services, url_prefix="/")
    app.register_blueprint(appointments, url_prefix="/")

    from hairArtProject.models import Appointments, Customer, Services

    with app.app_context():
        db.create_all()

    return app


def create_database(app):
    """creates database instances"""
    if not path.exists("hairArtProject/" + DB_NAME):
        db.create_all(app=app)
