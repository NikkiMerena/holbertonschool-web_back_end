#!/usr/bin/env python3
"""This module contains a Flask app that serves a JSON response
"""
from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

# Initialize the Flask application
app = Flask(__name__)

# Instantiate Auth object
AUTH = Auth()

# Define a route for the root URL ("/") using the route
# decorator and the associated function


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response(
            jsonify({"email": email, "message": "logged in"}), 200)
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
