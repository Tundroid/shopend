#!/usr/bin/python3
""" Subject API endpoints """

from flask import abort, request, jsonify
from models.subject import Subject
from models import storage
from api.v1.views import app_views


@app_views.route("/subjects", methods=['GET'], strict_slashes=False)
@app_views.route("/subjects/<subject_id>", methods=['GET'], strict_slashes=False)
def get_subjects(subject_id=None):
    if subject_id:
        subject = storage.get(Subject, subject_id)
        if subject:
            return subject.to_dict()
        abort(404)

    """get all subjects"""
    subjects = [obj.to_dict() for obj in storage.all(Subject).values()]
    return jsonify(subjects)


@app_views.route("/subjects/<subject_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_subject(subject_id):
    """ deletes a subject by id if it exist else raise 404"""
    subject = storage.get(Subject, subject_id)
    if subject:
        subject.delete()
        storage.save()
        return {}
    abort(404)


@app_views.route("/subjects", methods=['POST'], strict_slashes=False)
def create_subject():
    """method to create a new subject"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    if 'title' not in data:
        abort(400, "Missing title")
    subject = Subject(**data)
    subject.save()

    return subject.to_dict(), 201


@app_views.route("/subjects/<subject_id>", methods=['PUT'], strict_slashes=False)
def update_subject(subject_id):
    """method to update subject by id"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    subject = storage.get(Subject, subject_id)
    if subject:
        for key, val in data.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(subject, key, val)
        subject.save()
        return subject.to_dict(), 200
    abort(404)
