#!/usr/bin/python3
""" Candidate API endpoints """

from flask import abort, request
from models.candidate import Candidate
from models import storage
from api.v1.views import app_views, format_response


@app_views.route("/candidates", methods=['GET'], strict_slashes=False)
@app_views.route("/candidates/<candidate_id>", methods=['GET'], strict_slashes=False)
def get_candidates(candidate_id=None):
    if candidate_id:
        candidate = storage.get(Candidate, candidate_id)
        if candidate:
            return candidate.to_dict()
        abort(404)

    """get all candidatedssss"""
    candidates = [obj.to_dict() for obj in storage.all(Candidate).values()]
    return format_response(candidates)


@app_views.route("/candidates/<candidate_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_candidate(candidate_id):
    """ deletes a candidate by id if it exist else raise 404"""
    candidate = storage.get(Candidate, candidate_id)
    if candidate:
        candidate.delete()
        storage.save()
        return {}
    abort(404)


@app_views.route("/candidates", methods=['POST'], strict_slashes=False)
def create_candidate():
    """method to create a new candidate"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    if 'first_name' not in data:
        abort(400, "Missing first_name")
    if 'middle_name' not in data:
        abort(400, "Missing middle_name")
    if 'last_name' not in data:
        abort(400, "Missing last_name")
    candidate = Candidate(**data)
    candidate.save()

    return candidate.to_dict(), 201


@app_views.route("/candidates/<candidate_id>", methods=['PUT'], strict_slashes=False)
def update_candidate(candidate_id):
    """method to update candidate by id"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    candidate = storage.get(Candidate, candidate_id)
    if candidate:
        for key, val in data.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(candidate, key, val)
        candidate.save()
        return candidate.to_dict(), 200
    abort(404)
