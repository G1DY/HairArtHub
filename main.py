#!/usr/bin/env python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


if __name__ == '__main__':
    app.run(HOST='0.0.0.0', PORT='5000')
