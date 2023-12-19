#!/usr/bin/env python3
"""authetication module"""
from flask import (Blueprint, flash, jsonify, redirect, render_template,
                   request, session, url_for)

from hairArtProject.models import Appointments, Customer, Services

# from . import db


appointments = Blueprint("appointments", __name__)

@appointments.route('/booking', methods=['POST', 'GET'])
def booking():
    if request.method == 'POST':
        service = request.form['service']
        selected_time = request.form['selected_time']
        username = session['name']
        found_user = Customer.query.filter_by(name=username).first()
        customer_id = found_user.customer_id
        found_services = Services.query.filter_by(service_name=service).first()
        price = found_services.price

        if not Appointments.query.filter_by(appointment_timee=selected_time, which_service=service).first():
            new_booking = Appointments(which_service=service, which_customer=customer_id, appointment_time=selected_time)
            db.session.add(new_booking)
            db.session.commit()
            flash('Booking successful!', 'success')
            return redirect(url_for('payments'))
        else:
            flash('Time slot not available. Please choose another time.', 'danger')
            return redirect(url_for('appointments'))
    else:
        return render_template('booking.html')

@appointments.route('/payments', methods= ['POST', 'GET'])
def payments():
    if request.methods == 'POST':
        pass
    else:
        return render_template('payments.html')

        

