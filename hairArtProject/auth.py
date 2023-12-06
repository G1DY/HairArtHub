#!/usr/bin/env python3
"""authetication module"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Customer
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user

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
                flash("Logged in Successfully", category="success")
                login_user(user, remember=True)
            else:
                flash("Incorrect Password, try again", category="error")
        else:
            flash("Email does not exist", category="error")
    return render_template("login.html")


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
            flash("User already exists", category="error")
        elif not email or len(email) < 5 or "@" not in email:
            flash("Email must have atleast 5 characters", category="error")
        elif len(username) < 5 or not username:
            flash("Username must have atleats 5 characters", category="error")
        elif password != _password:
            flash("Password do not match", category="error")
        elif len(password) < 7 or len(_password) < 7:
            flash("Password too short", category="error")
        else:
            new_user = User(
                email=email,
                username=username,
                password=generate_password_hash(password, method="sha256"),
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))

    return render_template("sign_up.html")
