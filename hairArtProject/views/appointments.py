#!/usr/bin/env python3
"""authetication module"""
from flask import Blueprint, jsonify, redirect, request, session

from hairArtProject import db
from hairArtProject.models import Appointments, Customer, Services

appointments = Blueprint("appointments", __name__)

@appointments.route('/create_bookings', methods=['POST', 'GET'])
def create_booking():
    """books a service"""
    if request.method == 'POST':
        """Check if 'name' key exists in the session"""
        if 'name' in session:
            username = session['name']
            found_user = Customer.query.filter_by(name=username).first()

            """Check if the user exists"""
            if found_user:
                customer_id = found_user.customer_id
                service = request.json['service']
                selected_time = request.json['selected_time']

                found_services = Services.query.filter_by(service_name=service).first()
                price = found_services.price

                """Check if the selected time for the service is available"""
                if not Appointments.query.filter_by(appointment_time=selected_time, which_service=service).first():
                    new_booking = Appointments(which_service=service, which_customer=customer_id, appointment_time=selected_time)
                    db.session.add(new_booking)
                    db.session.commit()
                    return jsonify({"message": "Booking successful!"}), 200
                else:
                    return jsonify({"message": "Time slot not available, choose another time."}), 403
            else:
                return jsonify({"message": "User not found."}), 404
        else:
            return jsonify({"message": "User not authenticated."}), 401

@appointments.route('/view_bookings', methods=['POST', 'GET'])
def view_bookings():

    return jsonify({})


@appointments.route('/update_bookings', methods=['POST', 'GET'])
def update_booking():

    return jsonify({})


@appointments.route('/payments', methods= ['POST', 'GET'])
def payments():
    if request.methods == 'POST':
        pass
    else:
        return jsonify({})

        

