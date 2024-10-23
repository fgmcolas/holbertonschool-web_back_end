#!/usr/bin/env python3
""" Route module for the API - Mock logging in"""


from flask import Flask, request, render_template, g
from flask_babel import Babel
from os import getenv
from typing import Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Setup - Babel configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_locale():
    """ Determines best match for supported languages """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ Returns a user dictionary or None if the ID
    cannot be found or if login_as was not passed.
    """
    user_id = request.args.get('login_as')
    if user_id is not None:
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """ Set user globally before each request """
    g.user = get_user()


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """ GET /
    Return: 5-index.html
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
