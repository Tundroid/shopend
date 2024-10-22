#!/usr/bin/python3
""" Model creator API endpoints """

from flask import request, jsonify, abort
from models.engine.db_storage import classes_commerce, classes_account
from models import storage
from api.v1.views import app_views
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError
from models.base_model import Database

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

        data = [data] if type(data) is dict else data
        db = Database.COMMERCE if classes[model] in classes_commerce.values() else Database.ACCOUNT
        with storage.transaction(db) as session:
            for piece in data:
                db_model = classes[model](**piece)
                session.new(db_model, db=db)
                # session.save(db=db)
        
        return jsonify(db_model.to_dict()), 201
    except (KeyError, ValueError) as e:
        return  abort(404, description=f"Model `{model}`")
    except (IntegrityError) as e:
        return  abort(409, description=f"Resource already exists in Model `{model}`")
