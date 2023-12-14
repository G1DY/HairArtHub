from datetime import datetime
from . import db


class Customer(db.Model):
    """the customer table"""

    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    gender = db.Column(db.CHAR)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"


class Services(db.Model):
    """the services available"""

    service_id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String, unique=True, nullable=True)
    duration = db.Column(db.DateTime, unique=False, nullable=False)
    booked_time = db.Column(db.DateTime, nullable=False, unique=True)
    price = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f"Services('{self.service_id}', '{self.service_name}')"


class Appointments(db.Model):
    """Customer Appointments"""

    appointment_id = db.Column(db.Integer, primary_key=True)
    which_service = db.Column(db.String(20), unique=True, nullable=False)
    details = db.Column(db.String, unique=True, nullable=True)
    which_customer = db.Column(db.DateTime, unique=True, nullable=False)
    appointment_time = db.Column(
        db.DateTime, unique=True, nullable=False, default=datetime.utcnow
    )

    def __repr__(self):
        return f"Appointments('{self.appointment_id}', '{self.which_service}')"
