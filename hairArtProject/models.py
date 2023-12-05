from datetime import datetime
from hairArtProject import db 


class Customer(db.Model):
    '''the customer table'''
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    gender = db.Column(db.CHAR)
    bookings = db.relationship('Appointments', backref='clientBookings')


    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"


class Services(db.Model):
    '''the services available'''
    service_id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String, unique=True, nullable=True)
    duration = db.Column(db.String, unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    clientService = db.relationship('Appointments', backref='client_service')

    def __repr__(self):
        return f"User('{self.service_id}', '{self.service_name}')"

class Appointments(db.Model):
    '''Customer Appointments'''
    appointment_id = db.Column(db.Integer, primary_key=True)
    which_service = db.Column(db.Integer, db.ForeignKey('services.service_id'), unique=False, nullable=True)
    details = db.Column(db.String, unique=True, nullable=True)
    which_customer = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), unique=False, nullable=False)
    appointment_time = db.Column(db.DateTime, unique=True, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Appointments('{self.which_customer}', '{self.which_service}')"