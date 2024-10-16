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
    """Retrieve model or model instance details.

    Args:
        model (str): The model name.
        model_id (str): The ID of the model instance (optional).

    Returns:
        JSON response with model data or an error message.
    """
    if (not model):
        return jsonify({"type": "error", "message": "Model is required"}), 400
    
    try:
        if model_id:
            model = storage.get(classes[model], model_id)
            if model:
                return model.to_dict()
            return jsonify({"type": "error", "message": f"Model {model} identified by {model_id} not found"}), 404

        """get all @model details"""
        models = [obj.to_dict() for obj in storage.all(classes[model]).values()]
        return jsonify(models)
    except (KeyError):
        return jsonify({"type": "error", "message": f"Model {model} not found"}), 404

