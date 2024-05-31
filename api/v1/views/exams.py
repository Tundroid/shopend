#!/usr/bin/python3
""" Exam API endpoints """

from flask import abort, request
from models.exam import Exam
from models import storage
from api.v1.views import app_views, format_response


@app_views.route("/exams", methods=['GET'], strict_slashes=False)
@app_views.route("/exams/<exam_id>", methods=['GET'], strict_slashes=False)
def get_exams(exam_id=None):
    if exam_id:
        exam = storage.get(Exam, exam_id)
        if exam:
            return exam.to_dict()
        abort(404)

    """get all exams"""
    exams = [obj.to_dict() for obj in storage.all(Exam).values()]
    return format_response(exams)


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


@app_views.route("/exams", methods=['POST'], strict_slashes=False)
def create_exam():
    """method to create a new exam"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    if 'exam_name' not in data:
        abort(400, "Missing exam_name")
    if 'exam_abbrev' not in data:
        abort(400, "Missing exam_abbrev")
    exam = Exam(**data)
    exam.save()

    return exam.to_dict(), 201


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
