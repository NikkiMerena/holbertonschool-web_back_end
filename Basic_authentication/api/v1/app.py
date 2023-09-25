#!/usr/bin/env python3
"""
Route module for the API
"""
import os
from os import getenv

from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)

from api.v1.views import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = os.getenv("AUTH_TYPE")

if auth_type == "auth":
    auth = Auth()
elif auth_type == "basic_auth":
    auth = BasicAuth()


@app.before_request
def before_request_func():
    """Handling before_request."""
    if auth is None:
        return

    # List of paths that don't need authentication
    exempt_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                    '/api/v1/forbidden/']

    # Check if request.path is not in the exempt_paths
    if not auth.require_auth(request.path, exempt_paths):
        return

    # If auth.authorization_header(request) returns None, raise the error 401
    if auth.authorization_header(request) is None:
        abort(401)

    # If auth.current_user(request) returns None, raise the error 403
    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_error(error):
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error):
    """Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
    app.run(debug=True)
