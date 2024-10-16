#!/usr/bin/python3
""" Candidate API endpoints """

from flask import abort, request, jsonify
from models.admin import Admin
from models.depot_detail import AdminSession
from models import storage
from api.v1.views import app_views
import hashlib

# def require_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth_header = request.headers.get('Authorization')
#         if not auth_header:
#             return jsonify({'message': 'Missing Authorization Header'}), 401
#         parts = auth_header.split(" ")
#         if len(parts) != 2 or parts[0].lower() != 'bearer':
#             return jsonify({'message': 'Invalid Authorization Header'}), 401
#         admin_sess = storage.get(AdminSession, parts[1])
#         if admin_sess:
#             if (admin_sess.expired()):
#                 return jsonify({'error': 'Session expired'}), 401
#         else:
#             return jsonify({'error': 'Unknown session'}), 401
#         return f(*args, **kwargs)
#     return decorated


@app_views.route("/admins", methods=['GET'], strict_slashes=False)
@app_views.route("/admins/<admin_id>", methods=['GET'], strict_slashes=False)
def get_admins(admin_id=None):
    if admin_id:
        admin = storage.get(Admin, admin_id)
        if admin:
            return admin.to_dict()
        abort(404)

    """ get all admins """
    admins = [obj.to_dict() for obj in storage.all(Admin).values()]
    return jsonify(admins)


@app_views.route("/admins/login", methods=['POST'], strict_slashes=False)
def login_admin():
    """method to login admin"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    if 'admin_id' not in data:
        abort(400, "Missing admin_id")
    if 'admin_pass' not in data:
        abort(400, "Missing admin_pass")

    admin = storage.get(Admin, data['admin_id'])
    if admin:
        admin_pass = data['admin_pass'].encode('utf-8')
        sha512_hash = hashlib.sha512()
        sha512_hash.update(admin_pass)
        hash_hex = sha512_hash.hexdigest()
        if (admin.password == hash_hex):
            admin_sess = AdminSession(**{"admin": admin.admin_id})
            admin_sess.save()
            return jsonify(admin_sess.to_dict()), 201
        else:
            return jsonify({"error": "password incorrect"}), 401
    return jsonify({"error": "admin not found"}), 401

@app_views.route("/admins/sessions/", methods=['GET'], strict_slashes=False)
@app_views.route("/admins/sessions/<ses_id>", methods=['GET'], strict_slashes=False)
def get_admin_sessions(ses_id=None):
    if ses_id:
        session = storage.get(AdminSession, ses_id)
        if session:
            return admin.to_dict()
        abort(404)

    """ get all admins """
    sessions = [obj.to_dict() for obj in storage.all(AdminSession).values()]
    return jsonify(sessions)


# @app_views.route("/candidates/<candidate_id>", methods=['DELETE'],
#                  strict_slashes=False)
# def delete_candidate(candidate_id):
#     """ deletes a candidate by id if it exist else raise 404"""
#     candidate = storage.get(Candidate, candidate_id)
#     if candidate:
#         candidate.delete()
#         storage.save()
#         return {}
#     abort(404)


# @app_views.route("/candidates", methods=['POST'], strict_slashes=False)
# def create_candidate():
#     """method to create a new candidate"""
#     data = request.get_json(silent=True)
#     if data is None:
#         abort(400, "Not a JSON")
#     if 'first_name' not in data:
#         abort(400, "Missing first_name")
#     if 'middle_name' not in data:
#         abort(400, "Missing middle_name")
#     if 'last_name' not in data:
#         abort(400, "Missing last_name")
#     candidate = Candidate(**data)
#     candidate.save()

#     return candidate.to_dict(), 201


# @app_views.route("/candidates/<candidate_id>", methods=['PUT'], strict_slashes=False)
# def update_candidate(candidate_id):
#     """method to update candidate by id"""
#     data = request.get_json(silent=True)
#     if data is None:
#         abort(400, "Not a JSON")
#     candidate = storage.get(Candidate, candidate_id)
#     if candidate:
#         for key, val in data.items():
#             if key not in ["id", "created_at", "updated_at"]:
#                 setattr(candidate, key, val)
#         candidate.save()
#         return candidate.to_dict(), 200
#     abort(404)
