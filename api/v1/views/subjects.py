#!/usr/bin/python3
""" ViewSubjectRegistration API endpoints """

from flask import abort, request, jsonify
from models.view_subject import ViewSubject
from models import storage
from api.v1.views import app_views, format_response


@app_views.route("/subjects", methods=['GET'], strict_slashes=False)
@app_views.route("/subjects/<exam_id>", methods=['GET'], strict_slashes=False)
def get_subjects(exam_id=None):
    subjects = None
    if exam_id:
        subjects = [obj.to_dict() for obj in storage.all(ViewSubject, f"ViewSubject.exam == '{exam_id}'").values()]
        if not subjects:
            abort(404)
    else:
        """get all subjects"""
        subjects = [obj.to_dict() for obj in storage.all(ViewSubject).values()]
    response = jsonify(subjects)
    # return format_response(registrations)
    return response
