#!/usr/bin/python3
""" Exam API endpoints """

from flask import abort, request, jsonify
from models.operation import Operation
from models import storage
from api.v1.views import app_views


@app_views.route("/operation", methods=['GET'], strict_slashes=False)
@app_views.route("/operation/<operation_id>", methods=['GET'], strict_slashes=False)
def get_operation(operation_id=None):
    if operation_id:
        print("hmmm", operation_id)
        operation = storage.get(Operation, operation_id)
        if operation:
            return operation.to_dict()
        abort(404)

    """ get all operations """
    operations = [obj.to_dict() for obj in storage.all(Operation).values()]
    return jsonify(operations)

