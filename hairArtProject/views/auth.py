#!/usr/bin/env python3
"""authetication module"""
from flask import (Blueprint, flash, jsonify, redirect, render_template,
                   request, url_for)
from flask_login import current_user, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

from hairArtProject import DB_NAME, db
from hairArtProject.models import Customer, User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    """takes user name and password"""
    if request.method == "POST":
        email = request.json.get("email")
        password = request.json.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return jsonify({"message": "Logged in Successfully"}), 200
                
            else:
                return jsonify({"message": "Incorrect Password, try again"})
        else:
            return jsonify({"message": "Email does not exist"}), 201
    return jsonify({"message": "Welcome to login page"})


@auth.route("/logout", methods=["POST", "GET"], strict_slashes=False)
@login_required
def logout():
    """logs out a user"""
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["POST", "GET", "DELETE"], strict_slashes=False)
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
            password=generate_password_hash(password, method="pbkdf2:sha256"),
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)

        # If using redirect instead of JSON response
        # return redirect(url_for("views.home"))

        return jsonify({"message": "Account created!"}), 200

    return jsonify({"message": "Welcome to the home page"}), 200
