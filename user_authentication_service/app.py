#!/usr/bin/env python3
"""summary
"""
from flask import Flask, jsonify, request, abort
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
