#!/usr/bin/env python3
"""authetication module"""
from flask import Blueprint, jsonify, redirect, request, session, url_for
from flask_login import login_required, login_user, logout_user

from .. import db
from ..models import Customer, User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"], strict_slashes=False)
def login():
    """Takes email and password for user login"""
    if request.method == "POST":
        username = request.json.get("username")
        session['username'] = username
        password = request.json.get("password")

        # try:
        user = User.query.filter_by(username=username).first()
        if user:
            if user.check_password(password):
                token = user.encode_auth_token(user.user_id)
                # print(token)
                # import pdb; pdb.set_trace()
                # login_user(user, remember=True)
                return jsonify({"message": "Logged in Successfully",
                                "token": token.decode()}), 200
            else:
                return jsonify({"error": "Unauthorized Password, try again"}), 401
        else:
            return jsonify({"error": "Account Not Found, Please Sign Up"}), 404
        
    return redirect(url_for('auth.sign_up'))
        # except Exception as e:
        #     print(f"Error: {str(e)}")
        #     return jsonify({"error": "Internal Server Error"}), 500


@auth.route("/logout", methods=["POST", "GET"], strict_slashes=False)
@login_required
def logout():
    """logs out a user"""
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign_up", methods=["POST", "GET", "DELETE"], strict_slashes=False)
def sign_up():
    """Collects user information"""
    if request.method == "POST":
        email = request.json.get("email")
        username = request.json.get("username") or ""
        password = request.json.get("password")
        _password = request.json.get("_password")

        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({"error": "Email is already in use"}), 400

        if not email or len(email) < 5:
            return jsonify({"error": "Email must have at least 5 characters"}), 400

        if len(username) < 5 or not username:
            return jsonify({"error": "Username must have at least 5 characters"}), 400

        if password != _password:
            return jsonify({"error": "Passwords do not match"}), 400

        if len(password) < 7 or len(_password) < 7:
            return jsonify({"error": "Password is too short"}), 400

        new_user = User(
            email=email,
            username=username,
            password=password,
        )
        new = Customer(
            email=email,
            username=username,
            password=password,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)

        return jsonify({"message": "Account created!"}), 200

    return jsonify({"message": "Welcome to the home page"}), 200
