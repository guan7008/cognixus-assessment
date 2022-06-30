# load libraries
import os

# import mysql.connector
from flask import Flask, jsonify, request

# load modules
from endpoints.blueprint_auth import blueprint_auth
from endpoints.blueprint_todo import blueprint_todo

# init Flask app
app = Flask(__name__)

# middleware
@app.before_request
def authorized():
    headers = request.headers
    api_key = headers.get("X-API-KEY")
    if api_key != os.environ["API_KEY"]:
        return jsonify(
            {
                "message": "ERROR: Unauthorized",
            },
            401,
        )


# register blueprints
app.register_blueprint(
    blueprint_auth,
    url_prefix="/api/v1/auth",
)
app.register_blueprint(
    blueprint_todo,
    url_prefix="/api/v1/todo",
)
