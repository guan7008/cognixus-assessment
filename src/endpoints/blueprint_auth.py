import os
import validators
import google.oauth2.credentials
import googleapiclient.discovery
from crypt import methods
from flask import Blueprint, jsonify, request
from authlib.client import OAuth2Session

# define the blueprint
blueprint_auth = Blueprint(name="blueprint_auth", import_name=__name__)

GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]
GOOGLE_PROJECT_ID = os.environ["GOOGLE_PROJECT_ID"]
GOOGLE_AUTH_URI = os.environ["GOOGLE_AUTH_URI"]
GOOGLE_TOKEN_URI = os.environ["GOOGLE_TOKEN_URI"]
GOOGLE_AUTH_PROVIDER_X509_CERT_URL = os.environ["GOOGLE_AUTH_PROVIDER_X509_CERT_URL"]
GOOGLE_CLIENT_SECRET = os.environ["GOOGLE_CLIENT_SECRET"]
GOOGLE_REDIRECT_URI = os.environ["GOOGLE_REDIRECT_URI"]
AUTHORIZATION_SCOPE = "openid email profile"


@blueprint_auth.route("/google/login", methods=["POST"])
def google_login():
    # retrieve body data from input JSON
    redirect_uri = request.form.get("redirect_uri")

    if not redirect_uri or not validators.url(redirect_uri):
        return jsonify(
            {
                "status_code": 21001,
                "message": "ERROR: Invalid Input",
            }
        )

    session = OAuth2Session(
        GOOGLE_CLIENT_ID,
        GOOGLE_CLIENT_SECRET,
        scope=AUTHORIZATION_SCOPE,
        redirect_uri=redirect_uri,
    )

    uri = session.authorization_url(GOOGLE_AUTH_URI)
    return jsonify(
        {
            "status_code": 20000,
            "message": "OK: Proceed To Login Uri",
            "redirect_uri": uri,
        }
    )
