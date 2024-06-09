#!/usr/bin/python3
""" ViewExamRegistration API endpoints """

from flask import abort, request, jsonify
from models.view_exam_registration import ViewExamRegistration
from models import storage
from api.v1.views import app_views, format_response


@app_views.route("/registrations", methods=['GET'], strict_slashes=False)
@app_views.route("/registrations/<gce_id>", methods=['GET'], strict_slashes=False)
def get_registrations(gce_id=None):
    registrations = None
    if gce_id:
        registrations = [obj.to_dict() for obj in storage.all(ViewExamRegistration, f"ViewExamRegistration.candidate == '{gce_id}'").values()]
        if not registrations:
            abort(404)
    else:
        """get all registrations"""
        registrations = [obj.to_dict() for obj in storage.all(ViewExamRegistration).values()]
    response = jsonify(registrations)
    # return format_response(registrations)
    return response
