#!/usr/bin/python3
""" Model getter API endpoints """

from flask import abort, request, jsonify
from models.family import Family
from models.depot_detail import DepotDetail
from models.operation import Operation
from models import storage
from api.v1.views import app_views

classes = {"depot_detail": DepotDetail, "operation": Operation, "family": Family}


@app_views.route("/get", methods=['GET'], strict_slashes=False)
@app_views.route("/get/<model>", methods=['GET'], strict_slashes=False)
@app_views.route("/get/<model>/<model_id>", methods=['GET'], strict_slashes=False)
def get_model(model=None, model_id=None):
    if (not model):
        abort(400) # bad request
    
    try:
        if model_id:
            model = storage.get(classes.get(model), model_id)
            if model:
                return model.to_dict()
            abort(404)

        """get all @model details"""
        models = [obj.to_dict() for obj in storage.all(classes.get(model)).values()]
        return jsonify(models)
    except (KeyError):
        abort(404) # model not found

