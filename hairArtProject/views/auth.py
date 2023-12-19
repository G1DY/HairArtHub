#!/usr/bin/env python3
"""authetication module"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from hairArtProject.models import Customer
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from flask import jsonify

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    """takes user name and password"""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = Customer.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                return jsonify({"message": "Logged in Successfully"})
                login_user(user, remember=True)
            else:
                return jsonify({"message": "Incorrect Password, try again"})
        else:
            return jsonify({"message": "Email does not exist"})
    return jsonify({"message": "Welcome to login page"})


@auth.route("/logout", methods=["POST", "GET"], strict_slashes=False)
@login_required
def logout():
    """logs out a user"""
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["POST", "GET"], strict_slashes=False)
def sign_up():
    """collects user information"""
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username") or ""
        password = request.form.get("password")
        _password = request.form.get("_password")

        user = Customer.query.filter_by(email=email).first()
        if user:
            flash({"message": "User already exists"})
        elif not email or len(email) < 5 or "@" not in email:
            return jsonify({"message": "Email must have atleast 5 characters"})
        elif len(username) < 5 or not username:
            return jsonify({"message": "Username must have atleats 5 characters"})
        elif password != _password:
            return jsonify({"message": "Password do not match"})
        elif len(password) < 7 or len(_password) < 7:
            return jsonify({"message": "Password too short"})
        else:
            new_user = User(
                email=email,
                username=username,
                password=generate_password_hash(password, method="sha256"),
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            return jsonify({"message": "Account created!"})
            # return redirect(url_for("views.home"))

    return jsonify({"message": "Welcome to home page"})
