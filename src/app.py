# load libraries
import os

# import mysql.connector
from flask import Flask, jsonify, request

# load modules
from endpoints.blueprint_auth import blueprint_auth
from endpoints.blueprint_data import blueprint_data

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
                "status_code": 20001,
                "message": "ERROR: Unauthorized",
            },
        )


# register blueprints
app.register_blueprint(
    blueprint_auth,
    url_prefix="/api/v1/auth",
)
app.register_blueprint(
    blueprint_data,
    url_prefix="/api/v1/data",
)
