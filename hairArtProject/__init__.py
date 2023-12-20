#!/usr/bin/env python3
from os import path

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "users.db"
migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "uniquepassword"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    migrate.init_app(app, db)


    from hairArtProject.views.appointments import appointments
    from hairArtProject.views.auth import auth
    from hairArtProject.views.services import services

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(services, url_prefix="/")
    app.register_blueprint(appointments, url_prefix="/")

    from hairArtProject.models import Appointments, Customer, Services, User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager(app)
    login_manager.login_view = 'login'  # Specify the login view
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    """creates database instances"""
    if not path.exists(f"hairArtProject/{DB_NAME}"):
        db.create_all(app=app)
