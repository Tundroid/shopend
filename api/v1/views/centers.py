#!/usr/bin/python3
""" Session API endpoints """

from flask import abort, request
from models.session import Session
from models import storage
from api.v1.views import app_views, format_response


@app_views.route("/sessions", methods=['GET'], strict_slashes=False)
@app_views.route("/sessions/<session_id>", methods=['GET'], strict_slashes=False)
def get_sessions(session_id=None):
    if session_id:
        session = storage.get(Session, session_id)
        if session:
            return session.to_dict()
        abort(404)

    """get all sessions"""
    sessions = [obj.to_dict() for obj in storage.all(Session).values()]
    return format_response(sessions)


@app_views.route("/sessions/<session_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_session(session_id):
    """ deletes a session by id if it exist else raise 404"""
    session = storage.get(Session, session_id)
    if session:
        session.delete()
        storage.save()
        return {}
    abort(404)


@app_views.route("/sessions", methods=['POST'], strict_slashes=False)
def create_session():
    """method to create a new session"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    if 'center_name' not in data:
        abort(400, "Missing center_name")
    session = Session(**data)
    session.save()

    return session.to_dict(), 201


@app_views.route("/sessions/<session_id>", methods=['PUT'], strict_slashes=False)
def update_session(session_id):
    """method to update session by id"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    session = storage.get(Session, session_id)
    if session:
        for key, val in data.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(session, key, val)
        session.save()
        return session.to_dict(), 200
    abort(404)
