#!/usr/bin/python3
"""API main routes"""

from flask import jsonify

from api.v1.views import app_views
from models import storage
from models.engine.db_storage import classes_account, classes_commerce


from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

from ..app import users

# Route to authenticate users and generate a JWT token
@app_views.route('/login', methods=['POST'])
def login():
    # Get Basic Auth credentials
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"msg": "Basic authentication required"}), 401

    # Validate user credentials
    user = users.get(auth.username)
    if not user or not check_password_hash(user['password'], auth.password):
        return jsonify({"msg": "Invalid username or password"}), 401

    # Generate JWT token
    access_token = create_access_token(identity=auth.username)
    return jsonify(access_token=access_token), 200


@app_views.route("/status", strict_slashes=False)
def status():
    """Returns the status in JSON format"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stats():
    """Endpoint that retrieves the number of each objects by type"""
    stats_dict = {}
    classes = classes_commerce | classes_account
    for cls_name, cls in classes.items():
        stats_dict[cls_name] = storage.count(cls)
    return jsonify(stats_dict)
