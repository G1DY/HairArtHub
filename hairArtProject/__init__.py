# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Replace with your database URI
db = SQLAlchemy(app)

from app import routes  # Import routes after creating the Flask app instance
