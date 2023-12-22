#!/usr/bin/env python3
"""authetication module"""
from flask import Blueprint, jsonify, redirect, request, session

from hairArtProject import db
from hairArtProject.models import Appointments, Customer, Services, User

appointments = Blueprint("appointments", __name__)

@appointments.route('/create_bookings', methods=['POST', 'GET'])
def create_booking():
    """books a service"""
    if request.method == 'POST':
        """Check if 'name' key exists in the session"""
        if 'username' in session:
            username = session['username']
            found_user = User.query.filter_by(username=username).first()
            """Check if the user exists"""
            if found_user:
                user_id = found_user.user_id
                service = request.json.post['service']
                selected_time = request.json.post['selected_time']

                found_services = Services.query.filter_by(service_name=service).first()
                price = found_services.price

                """Check if the selected time for the service is available"""
                if not Appointments.query.filter_by(appointment_time=selected_time, which_service=service).first():
                    new_booking = Appointments(which_service=service, which_customer=user_id, appointment_time=selected_time, price=price)
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
    """View user's bookings"""
    if 'name' in session:
        username = session['username']
        found_user = User.query.filter_by(username=username).first()

        if found_user:
            user_id = found_user.user_id
            user_bookings = Appointments.query.filter_by(which_customer=user_id).all()

            bookings_data = []
            for booking in user_bookings:
                booking_info = {
                    'service': booking.service.service_name,
                    'appointment_time': booking.appointment_time.strftime("%Y-%m-%d %H:%M:%S")
                }
                bookings_data.append(booking_info)

            return jsonify({"bookings": bookings_data}), 200
        else:
            return jsonify({"message": "User not found."}), 404
    else:
        return jsonify({"message": "User not authenticated."}), 401

@appointments.route('/update_bookings', methods=['POST', 'GET'])
def update_booking():
    if request.method == 'POST':
        if 'username' not in session:
            return jsonify({"message": "User not authenticated."}), 401

        username = session['username']
        user = User.query.filter_by(username=username).first()

        if not user:
            return jsonify({"message": "User not found."}), 404

        user_id = user.user_id
        booking_id = request.json.get('booking_id')

        if not booking_id:
            return jsonify({"message": "Invalid request. 'booking_id' is required."}), 400

        booking = Appointments.query.filter_by(booking_id=booking_id, which_customer=user_id).first()

        if not booking:
            return jsonify({"message": "Booking not found or doesn't belong to the user."}), 404

        service = request.json.get('service')
        selected_time = request.json.get('selected_time')

        if not service or not selected_time:
            return jsonify({"message": "Invalid request. 'service' and 'selected_time' are required."}), 400

        existing_service = Services.query.filter_by(service_name=service).first()

        if not existing_service:
            return jsonify({"message": f"Service '{service}' not found."}), 404

        if Appointments.query.filter_by(appointment_time=selected_time, which_service=service).first():
            return jsonify({"message": "Time slot not available, choose another time."}), 403

        """Update the existing booking"""
        booking.which_service = service
        booking.appointment_time = selected_time
        booking.price = existing_service.price

        db.session.commit()
        return jsonify({"message": "Booking updated successfully!"}), 200

    elif request.method == 'GET':
        return jsonify({"message": "GET request received."}), 200

    return jsonify({"message": "Method not allowed."}), 405


@appointments.route('/payments', methods= ['POST', 'GET'])
def payments():
    if request.methods == 'POST':
        pass
    else:
        return jsonify({})

        

