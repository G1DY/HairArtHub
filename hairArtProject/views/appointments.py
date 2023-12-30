#!/usr/bin/env python3
"""authetication module"""
from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request

from hairArtProject.models import Appointments, Services, User
from hairArtProject.views.auth import session

from .. import db

appointments = Blueprint("appointments", __name__)

@appointments.route('/create_bookings', methods=['POST', 'GET'])
def create_booking():
    """books a service"""
    
    if request.method == 'POST':
        """Check if 'name' key exists in the session"""
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                responseObject = {
                    'status': 'fail',
                    'message': 'Bearer token malformed.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user_id = resp
                # user = User.query.filter_by(id=resp).first()
                found_user = User.query.filter_by(user_id=user_id).first()
                """Check if the user exists"""
            
                user_id = found_user.user_id
                service = request.json.get('service')
                selected_time = request.json.get('selected_time')
                appointment_time = datetime.strptime(selected_time, "%Y-%m-%d %H:%M:%S.%f")

                found_services = Services.query.filter_by(service_name=service).first()
                price = found_services.price

                """To fetch available appointment time:"""
                service_duration = found_services.duration
                new_duration = timedelta(days=0, hours=0, minutes=service_duration, seconds=0)   
                available_time = appointment_time + new_duration

                """Check if the selected time for the service is available"""
                if not Appointments.query.filter_by(appointment_time=selected_time, which_service=service).first():
                    new_booking = Appointments(which_service=service, which_customer=user_id, appointment_time=appointment_time, price=price)
                    db.session.add(new_booking)
                    db.session.commit()
                    return jsonify({"message": "Booking successful!"}), 200
                else:
                    response = jsonify({"message": f"Sorry. The time slot: {appointment_time} is not available. Kindly choose another time from {available_time}."})
                    response.status_code = 403
                    return response
            else:
                return jsonify({"message": "User not found."}), 404
        else:
            print(session)
            return jsonify({"message": "User not authenticated."}), 401       

@appointments.route('/view_bookings', methods=['POST', 'GET'])
def view_bookings():
    """View user's bookings"""
    if request.method == 'POST':
        if 'username' in session:
            # Get the username from the request body
            username = request.json.get('username')

            if not username:
                return jsonify({"message": "Username not provided in the request."}), 400

            found_user = User.query.filter_by(username=username).first()

            if found_user:
                user_id = found_user.user_id
                user_bookings = Appointments.query.filter_by(which_customer=user_id).all()

                bookings_data = []
                for booking in user_bookings:
                    booking_info = {
                        'service': booking.which_service,
                        'appointment_time': booking.appointment_time.strftime("%Y-%m-%d %H:%M:%S:%f")
                    }
                    bookings_data.append(booking_info)

                return jsonify({"bookings": bookings_data}), 200
            else:
                return jsonify({"message": "User not found."}), 404
        else:
            print(session)
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
        appointment_id = request.json.get('appointment_id')

        if not appointment_id:
            return jsonify({"message": "Invalid request. 'appointment_id' is required."}), 400

        booking = Appointments.query.filter_by(appointment_id=appointment_id, which_customer=user_id).first()

        if not booking:
            return jsonify({"message": "Booking not found or doesn't belong to the user."}), 404

        service = request.json.get('service')
        selected_time = request.json.get('selected_time')
        selected_time = datetime.strptime(selected_time, "%Y-%m-%d %H:%M:%S.%f")

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
    if request.method == 'POST':
        pass
    else:
        return jsonify({})

        

