from crypt import methods
from flask import Blueprint, jsonify, request

# define the blueprint
blueprint_auth = Blueprint(name="blueprint_auth", import_name=__name__)


@blueprint_auth.route("/login", methods=["POST"])
def login():
    return jsonify(
        {
            "message": "OK: Authorized",
        },
        200,
    )
