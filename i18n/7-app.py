#!/usr/bin/env python3
""" Route module for the API - Mock logging in"""


from flask import Flask, request, render_template, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError

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
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return (
        request.accept_languages.best_match(app.config['LANGUAGES']) or
        app.config['BABEL_DEFAULT_LOCALE']
    )


def get_timezone():
    """ Returns the user's timezone or UTC if not specified or invalid. """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


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


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/')
def index():
    """ GET /
    Return: 7-index.html
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run()
