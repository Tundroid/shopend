#!/usr/bin/python3
""" ViewExamRegistration API endpoints """

from flask import abort, request, jsonify
from models.view_exam_registration import ViewExamRegistration
from models import storage
from api.v1.views import app_views, check_auth_header


@app_views.route("/registrations", methods=['GET'], strict_slashes=False)
@app_views.route("/registrations/<gce_id>", methods=['GET'], strict_slashes=False)
def get_registrations(gce_id=None):
    registrations = None
    auth_check = None
    if gce_id:
        auth_check = check_auth_header()
        if (auth_check):
            return auth_check
        registrations = [obj.to_dict() for obj in storage.all(ViewExamRegistration, f"ViewExamRegistration.candidate == '{gce_id}'").values()]
        if not registrations:
            abort(404)
    else:
        """get all registrations"""
        auth_check = check_auth_header("AdminSession")
        if (auth_check):
            return auth_check
        registrations = [obj.to_dict() for obj in storage.all(ViewExamRegistration).values()]
    return jsonify(registrations)
