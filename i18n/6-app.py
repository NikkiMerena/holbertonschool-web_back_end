#!/usr/bin/env python3
"""Simple flask app with index.html template"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    # Additional users...
}

class Config():
    """Class which configures available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """Determine the best match with supported languages."""
    # 1. Locale from URL parameters
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    # 2. Locale from user settings
    elif g.get('user') and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    # 3. Locale from request header
    elif request.accept_languages.best_match(app.config['LANGUAGES']):
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    # 4. Default locale
    else:
        return app.config['BABEL_DEFAULT_LOCALE']

def get_user():
    """Return a user dictionary or None if the ID cannot be found or if login_as was not passed."""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None

@app.before_request
def before_request():
    """Find a user if any, and set it as a global on flask.g.user."""
    g.user = get_user()

@app.route('/', strict_slashes=False)
def index():
    """Route for `/`."""
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001")
