#!/usr/bin/python3
""" Subject Registrations API endpoints """

from flask import abort, request, jsonify
from models.subject_registration import SubjectRegistration
from models import storage
from api.v1.views import app_views, format_response


@app_views.route("/subject_registrations", methods=['GET'], strict_slashes=False)
@app_views.route("/subject_registrations/<exam_reg>", methods=['GET'], strict_slashes=False)
def get_subject_registrations(exam_reg=None):
    if exam_reg:
        sub = storage.get(SubjectRegistration, exam_reg)
        if sub:
            return sub.to_dict()
        abort(404)

    """get all exams"""
    subs = [obj.to_dict() for obj in storage.all(SubjectRegistration).values()]
    return jsonify(subs)


@app_views.route("/exams/<exam_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_exam(exam_id):
    """ deletes a exam by id if it exist else raise 404"""
    exam = storage.get(Exam, exam_id)
    if exam:
        exam.delete()
        storage.save()
        return {}
    abort(404)


@app_views.route("/subject_registrations", methods=['POST'], strict_slashes=False)
def create_subject_registration():
    """method to create a new exam"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    if 'exam_reg' not in data:
        abort(400, "Missing exam_reg")
    if 'exam_subj' not in data:
        abort(400, "Missing exam_subj")
    sub_reg = SubjectRegistration(**data)
    sub_reg.save()

    return sub_reg.to_dict(), 201


@app_views.route("/exams/<exam_id>", methods=['PUT'], strict_slashes=False)
def update_exam(exam_id):
    """method to update exam by id"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    exam = storage.get(Exam, exam_id)
    if exam:
        for key, val in data.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(exam, key, val)
        exam.save()
        return exam.to_dict(), 200
    abort(404)
