#!/usr/bin/python3
""" Model creator API endpoints """

from flask import request, jsonify, abort
from models.engine.db_storage import classes_commerce, classes_account
from models import storage
from api.v1.views import app_views
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

@app_views.route("/create", methods=['POST'], strict_slashes=False)
@app_views.route("/create/<model>", methods=['POST'], strict_slashes=False)
@jwt_required()
def create_model(model=None):
    """Create a new model instance.

    Args:
        model (str): The model name.
        request body: JSON data for the new model instance.

    Returns:
        JSON response with the created model data or an error message.
    """
    if (not model):
        abort(400, description="Model is required")

    try:
        classes = classes_commerce | classes_account
        data = request.get_json(silent=True)
        if not data:
            abort(400, description="Valid JSON data required")
        
        db_model = classes[model](**data)
        storage.new(db_model)
        storage.save()
        
        return jsonify(db_model.to_dict()), 201
    except (KeyError, ValueError) as e:
        return  abort(404, description=f"Model `{model}`")
    except (IntegrityError):
        return  abort(409, description=f"Resource already exists in Model `{model}`")


@app_views.route("/create/<model>/<foreign_key>", methods=['POST'], strict_slashes=False)
@jwt_required()
def create_model_foreign_key(model, foreign_key):
    """Create a new model instance with a foreign key.

    Args:
        model (str): The model name.
        foreign_key (str): The foreign key value.
        request body: JSON data for the new model instance.

    Returns:
        JSON response with the created model data or an error message.
    """
    try:
        classes = classes_commerce | classes_account
        data = request.get_json()
        if not data:
            abort(400, description="JSON data required")
        
        db_model = classes[model](**data, foreign_key=foreign_key)
        storage.new(db_model)
        storage.save()
        
        return jsonify(db_model.to_dict()), 201
    except (KeyError, ValueError) as e:
        return abort(400, description=str(e))
