#!/usr/bin/env python3
""" Route module for the API - Basic Babel setup """


from flask import Flask, request, render_template
from flask_babel import Babel
from os import getenv

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Setup - Babel configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET /
    Return: 1-index.html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
