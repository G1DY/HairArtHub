#!/usr/bin/env python3
"""authetication module"""
from flask import (Blueprint, flash, jsonify, redirect, render_template,
                   request, url_for)

from ..models import Services

# from appointments import booking

services = Blueprint("services", __name__)

@services.route('/services', methods= ['POST', 'GET'])
def services_route(service):
    if request.method == 'POST':
        return redirect(url_for('booking', service=service))
    else:
        return render_template('services.html')


