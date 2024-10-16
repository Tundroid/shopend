#!/usr/bin/python3
"""API main routes"""

from flask import jsonify

from api.v1.views import app_views
from models import storage
from models.engine.db_storage import classes


@app_views.route("/status", strict_slashes=False)
def status():
    """Returns the status in JSON format"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stats():
    """Endpoint that retrieves the number of each objects by type"""
    stats_dict = {}
    for cls_name, cls in classes.items():
        stats_dict[cls_name] = storage.count(cls)
    return jsonify(stats_dict)
