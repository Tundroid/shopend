#!/usr/bin/python3
""" Center API endpoints """

from flask import abort, request
from models.center import Center
from models import storage
from api.v1.views import app_views


@app_views.route("/centers", methods=['GET'], strict_slashes=False)
@app_views.route("/centers/<center_id>", methods=['GET'], strict_slashes=False)
def get_centers(center_id=None):
    if center_id:
        center = storage.get(Center, center_id)
        if center:
            return center.to_dict()
        abort(404)

    """get all centers"""
    centers = [obj.to_dict() for obj in storage.all(Center).values()]
    return jsonify(centers)


@app_views.route("/centers/<center_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_center(center_id):
    """ deletes a center by id if it exist else raise 404"""
    center = storage.get(Center, center_id)
    if center:
        center.delete()
        storage.save()
        return {}
    abort(404)


@app_views.route("/centers", methods=['POST'], strict_slashes=False)
def create_center():
    """method to create a new center"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    if 'center_name' not in data:
        abort(400, "Missing center_name")
    center = Center(**data)
    center.save()

    return center.to_dict(), 201


@app_views.route("/centers/<center_id>", methods=['PUT'], strict_slashes=False)
def update_center(center_id):
    """method to update center by id"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    center = storage.get(Center, center_id)
    if center:
        for key, val in data.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(center, key, val)
        center.save()
        return center.to_dict(), 200
    abort(404)
