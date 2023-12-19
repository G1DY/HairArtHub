from datetime import datetime

from . import db


class Customer(db.Model):
    """The customer table"""
    __tablename__ = 'customers'

    customer_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    gender = db.Column(db.CHAR)

    appointments = db.relationship('Appointments', backref='customer', lazy=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"


class Services(db.Model):
    """The services available"""

    service_id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String, unique=True, nullable=True)
    duration = db.Column(db.DateTime, unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)

    appointments = db.relationship('Appointments', backref='service', lazy=True)

    def __repr__(self):
        return f"Services('{self.service_id}', '{self.service_name}')"


class Appointments(db.Model):
    """Customer Appointments"""

    appointment_id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String, unique=True, nullable=True)
    which_customer = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    which_service = db.Column(db.Integer, db.ForeignKey('services.service_id'), nullable=False)
    appointment_time = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )

    def __repr__(self):
        return f"Appointments('{self.appointment_id}', '{self.which_service}', '{self.appointment_time}')"