#!/usr/bin/python3
""" Exam API endpoints """

from flask import abort, request, jsonify
from models.family import Family
from models import storage
from api.v1.views import app_views


@app_views.route("/family", methods=['GET'], strict_slashes=False)
@app_views.route("/family/<family_id>", methods=['GET'], strict_slashes=False)
def get_family(family_id=None):
    if family_id:
        family = storage.get(Family, family_id)
        if family:
            return family.to_dict()
        abort(404)

    """get all family details"""
    familys = [obj.to_dict() for obj in storage.all(Family).values()]
    return jsonify(familys)

