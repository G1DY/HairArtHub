#!/usr/bin/env python3
"""authetication module"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from hairArtProject.models import Services
from flask import jsonify
from appointments import booking

services = Blueprint("services", __name__)

@services.route('/services', methods= ['POST', 'GET'])
def services(service):
    if request.method == 'POST':
        return redirect(url_for('booking', service=service))
    else:
        return render_template('services.html')


