#!/usr/bin/python3
""" ViewSubjectRegistration API endpoints """

from flask import abort, request, jsonify
from models.view_subject_registration import ViewSubjectRegistration
from models import storage
from api.v1.views import app_views, format_response


@app_views.route("/candidate_subjects", methods=['GET'], strict_slashes=False)
@app_views.route("/candidate_subjects/<reg_id>", methods=['GET'], strict_slashes=False)
def get_candidate_subjects(reg_id=None):
    subjects = None
    if reg_id:
        subjects = [obj.to_dict() for obj in storage.all(ViewSubjectRegistration, f"ViewSubjectRegistration.reg == '{reg_id}'").values()]
        if not subjects:
            abort(404)
    else:
        """get all registrations"""
        subjects = [obj.to_dict() for obj in storage.all(ViewSubjectRegistration).values()]
    response = jsonify(subjects)
    # return format_response(registrations)
    return response
