#!/usr/bin/python3
"""Create a flask application for the API"""

from os import getenv

from flask import Flask, jsonify
from flask_cors import CORS

from models import storage
from api.v1.views import app_views
import os
from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
# CORS(app, resources={"/*": {"origins": "0.0.0.0"}})
CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(app_views)

# Configure the secret key for JWT
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_default_secret_key')  # Use environment variable in production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600 #datetime.timedelta(hours=1)  # Token expiration time: 1 hour
jwt = JWTManager(app)


@app.teardown_appcontext
def close(exception):
    """Closes the storage"""
    storage.close()


@app.errorhandler(404)
def not_found(e):
    '''Returns the JSON {"error": "Not found"} if resource wasn't found'''
    return {"error": "Not founds"}, e.code


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port="5000",
            threaded=True)
