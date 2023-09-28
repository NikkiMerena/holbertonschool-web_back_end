#!/usr/bin/env python3
"""summary
"""
from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the root URL ("/") using the route
# decorator and the associated function


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Bienvenue"})

# Add the code to run the Flask application


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
