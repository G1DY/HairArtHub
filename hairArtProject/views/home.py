#!/usr/bin/env python3
"""authetication module"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from hairArtProject.models import Customer
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from flask import jsonify

home = Blueprint("home", __name__)


@home.route("/", methods=["GET", "POST"], strict_slashes=False)
def home_route():
    return jsonify()
