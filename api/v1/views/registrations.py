#!/usr/bin/python3
""" ViewExamRegistration API endpoints """

from flask import abort, request, jsonify
from models.view_exam_registration import ViewExamRegistration
from models import storage
from api.v1.views import app_views, format_response


@app_views.route("/registrations", methods=['GET'], strict_slashes=False)
@app_views.route("/registrations/<reg_id>", methods=['GET'], strict_slashes=False)
def get_registrations(reg_id=None):
    if reg_id:
        registration = storage.get(ViewExamRegistration, reg_id)
        if registration:
            return registration.to_dict()
        abort(404)

    """get all registrationdssss"""
    registrations = [obj.to_dict() for obj in storage.all(ViewExamRegistration).values()]
    response = jsonify(registrations)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return format_response(registrations)
    return response


@app_views.route("/registrations/<reg_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_registration(reg_id):
    """ deletes a registration by id if it exist else raise 404"""
    registration = storage.get(ViewExamRegistration, reg_id)
    if registration:
        registration.delete()
        storage.save()
        return {}
    abort(404)


@app_views.route("/registrations", methods=['POST'], strict_slashes=False)
def create_registration():
    """method to create a new registration"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    if 'first_name' not in data:
        abort(400, "Missing first_name")
    if 'middle_name' not in data:
        abort(400, "Missing middle_name")
    if 'last_name' not in data:
        abort(400, "Missing last_name")
    registration = ViewExamRegistration(**data)
    registration.save()

    return registration.to_dict(), 201


@app_views.route("/registrations/<reg_id>", methods=['PUT'], strict_slashes=False)
def update_registration(reg_id):
    """method to update registration by id"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    registration = storage.get(ViewExamRegistration, reg_id)
    if registration:
        for key, val in data.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(registration, key, val)
        registration.save()
        return registration.to_dict(), 200
    abort(404)
