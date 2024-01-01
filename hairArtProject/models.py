from datetime import datetime, timedelta

import jwt
from flask_login import UserMixin
from sqlalchemy import Interval
from werkzeug.security import check_password_hash, generate_password_hash

from . import db


class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    customer = db.relationship('Customer', back_populates='user')

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.set_password(password)  # Use the method to set the password

    # @property
    # def password(self):
    #     return self.password

    def set_password(self, plaintext_password):
        self.password = generate_password_hash(plaintext_password, method="pbkdf2:sha256")

    def check_password(self, plaintext_password):
        print(check_password_hash(self.password, plaintext_password))
        return check_password_hash(self.password, plaintext_password)

    def get_id(self):
        return str(self.user_id)
    
    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=0, seconds=1200),
                'iat': datetime.utcnow(),
                'sub': user_id
            }

            return jwt.encode(
                payload,
                "gideon",
                algorithm='HS256'
            )
        except Exception as e:
            return e
        
    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, "gideon")
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
        

    

    @property
    def is_active(self):
        return True


class Customer(db.Model):
    """The customer table"""
    __tablename__ = 'customers'

    customer_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(255))
    phone = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.CHAR)

    user = db.relationship('User', back_populates='customer')
    appointments = db.relationship('Appointments', backref='customer', lazy=True)


class Services(db.Model):
    """The services available"""
    __tablename__ = 'services'

    service_id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String, unique=True, nullable=True)
    duration = db.Column(db.Integer, unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)

    appointments = db.relationship('Appointments', backref='service', lazy=True)

    def __repr__(self):
        return f"Services('{self.service_id}', '{self.service_name}', '{self.price}')"


class Appointments(db.Model):
    """Customer Appointments"""
    __tablename__ = 'appointments'

    appointment_id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, unique=False, nullable=False)
    which_customer = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    which_service = db.Column(db.Integer, db.ForeignKey('services.service_id'), nullable=False)
    appointment_time = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )

    def __repr__(self):
        return f"Appointments('{self.appointment_id}', '{self.which_service}', '{self.appointment_time}', '{self.price}')"
    
