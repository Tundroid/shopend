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
        abort(400, description="Model is required")
    
    try:
        if model_id:
            db_model = storage.get(classes[model], model_id)
            if db_model:
                return db_model.to_dict()
            abort(404, description=f"Model `{model}` identified by `{model_id}`")

        """get all @model details"""
        db_models = [obj.to_dict() for obj in storage.all(classes[model]).values()]
        return jsonify(db_models)
    except (KeyError):
        return  abort(404, description=f"Model `{model}`")
