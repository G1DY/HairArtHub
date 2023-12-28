#!/usr/bin/env python3
from os import path

from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Interval

#from hairArtProject.models import Appointments, Customer, Services, User
#from hairArtProject.models import *
db = SQLAlchemy()
DB_NAME = "users.db"
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.secret_key = "uniquepassword"
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    migrate.init_app(app, db)

    admin = Admin(app, name='hairArtProject', template_mode='bootstrap3')

    from .views.appointments import appointments
    from .views.auth import auth
    from .views.services import services
    

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(services, url_prefix="/")
    app.register_blueprint(appointments, url_prefix="/")

    from .models import Appointments, Customer, Services, User, timedelta

    with app.app_context():
        db.create_all()

    login_manager = LoginManager(app)
    login_manager.login_view = 'login'  # Specify the login view
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    with app.app_context():
        """
        s1 = Services(service_name='Line Up Haircut', description=None, duration=30, price=35.0)
        s2 = Services(service_name='Waves + Low Fade', description=None, duration=30, price=35.0)
        s3 = Services(service_name='Twisted Curls With Blow Out Fade', description=None, duration=30, price=35.0)
        s4 = Services(service_name='Frohawk', description=None, duration=30, price=35.0)
        s5 = Services(service_name='Faux Hawk With blonde Sponge Twists', description=None, duration=30, price=35.0)
        s6 = Services(service_name='Goddess Braids', description=None, duration=30, price=50.0)
        s7 = Services(service_name='Knotless Braids', description=None, duration=30, price=80.0)
        s8 = Services(service_name='Box Braids', description=None, duration=30, price=80.0)
        s9 = Services(service_name='Full body massage', description=None, duration=30, price=50.0)
        s10 = Services(service_name='Full body wax', description=None, duration=30, price=80.0)

        db.session.add(s1)
        db.session.add(s2)
        db.session.add(s3)
        db.session.add(s4)
        db.session.add(s5)
        db.session.add(s6)
        db.session.add(s7)
        db.session.add(s8)
        db.session.add(s9)
        db.session.add(s10)
        """
        # Services.query.delete()
        # Appointments.__table__.drop(db.engine)
        db.session.commit()

    return app
    print(s1)

    

def create_database(app):
    """creates database instances"""
    if not path.exists(f"hairArtProject/{DB_NAME}"):
        db.create_all(app=app)

