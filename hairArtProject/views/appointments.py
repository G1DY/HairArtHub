#!/usr/bin/env python3
"""authetication module"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from hairArtProject.models import Appointments
from flask import jsonify

appointments = Blueprint("appointments", __name__)
