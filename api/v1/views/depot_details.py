#!/usr/bin/python3
""" Exam API endpoints """

from flask import abort, request, jsonify
from models.depot_detail import DepotDetail
from models import storage
from api.v1.views import app_views


@app_views.route("/depot_detail", methods=['GET'], strict_slashes=False)
@app_views.route("/depot_detail/<depot_id>", methods=['GET'], strict_slashes=False)
def get_depot_detail(depot_id=None):
    print("Find me here")
    if depot_id:
        print("And here")
        depot_detail = storage.get(DepotDetail, depot_id)
        if depot_detail:
            return depot_detail.to_dict()
        abort(404)

    """get all depot details"""
    depot_details = [obj.to_dict() for obj in storage.all(DepotDetail).values()]
    return jsonify(depot_details)

