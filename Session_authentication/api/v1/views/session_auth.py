#!/usr/bin/env python3
"""
session_auth.py

This module contains the route handling and logic for
user session authentication.
It defines a Flask view that handles the POST /auth_session/login route.
The view authenticates the user based on their email and password, initiates a
new session if authentication is successful,
and sets the session ID in a cookie.

Classes:
    None

Functions:
    - session_auth: Authenticates user and initiates a session.
"""

from flask import Flask, request, jsonify, make_response, abort
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth():
    """
    Authenticate user and initiate a session.

    This view handles the POST /auth_session/login route and authenticates
    the user by verifying their email and password. If authentication is
    successful, a new session is created, and the session id is set in the
    cookie.

    :return: If authentication is successful, returns a JSON representation
            of the user. Otherwise, returns a JSON error message.
    """
    # Retrieve email from form data
    email = request.form.get('email')
    # Check if email is missing or empty
    if email is None or email.strip() == "":
        return jsonify({"error": "email missing"}), 400

    # Retrieve password from form data
    password = request.form.get('password')
    # Check if password is missing or empty
    if password is None or password.strip() == "":
        return jsonify({"error": "password missing"}), 400

    # Search for the user with the given email
    users = User.search({"email": email})
    # Check if no user is found for this email
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    # Retrieve the first user object from the list of users
    user = users[0]
    # Check if the password is not valid
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create a new session for the authenticated user
    session_id = auth.create_session(user.id)

    # Create a response object and set the session id in the cookie
    response = make_response(user.to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)

    # Return the response object
    return response


@app_views.route(
    '/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """Log out by destroying the user's session.

    This view handles the route for logging out a user by destroying
    their session. If the session is successfully destroyed, it returns a
    200 OK response; otherwise, it aborts the request with a 404 Not Found.

    Returns:
        Response: A Flask response object with a JSON payload, or a 404 abort.
    """
    if auth.destroy_session(request):
        return make_response(jsonify({}), 200)
    else:
        abort(404)
