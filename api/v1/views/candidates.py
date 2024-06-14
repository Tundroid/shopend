#!/usr/bin/python3
""" Candidate API endpoints """

from flask import abort, request, jsonify
from models.candidate import Candidate
from models.candidate_session import CandidateSession
from models import storage
from api.v1.views import app_views, format_response
import hashlib


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
    response = jsonify(candidates)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return format_response(candidates)
    return response


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

@app_views.route("/candidates/login", methods=['POST'], strict_slashes=False)
def login_candidate():
    """method to login candidate"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    if 'gce_id' not in data:
        abort(400, "Missing gce_id")
    if 'candidate_pass' not in data:
        abort(400, "Missing candidate_pass")

    candidate = storage.get(Candidate, data['gce_id'])
    if candidate:
        candidate_pass = data['candidate_pass'].encode('utf-8')
        sha512_hash = hashlib.sha512()
        sha512_hash.update(candidate_pass)
        hash_hex = sha512_hash.hexdigest()
        if (candidate.password == hash_hex):
            candidate_sess = CandidateSession(**{"candidate": candidate.candidate_id})
            candidate_sess.save()
            return jsonify(candidate_sess.to_dict()), 201
        else:
            return jsonify({"error": "password incorrect"}), 401
    return jsonify({"error": "candidate not found"}), 401

@app_views.route("/candidates/sessions/", methods=['GET'], strict_slashes=False)
@app_views.route("/candidates/sessions/<ses_id>", methods=['GET'], strict_slashes=False)
def get_candidate_sessions(ses_id=None):
    if ses_id:
        session = storage.get(CandidateSession, ses_id)
        if session:
            return candidate.to_dict()
        abort(404)

    """ get all candidates """
    sessions = [obj.to_dict() for obj in storage.all(CandidateSession).values()]
    return jsonify(sessions)