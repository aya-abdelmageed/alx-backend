#!/usr/bin/env python3
"""task 5"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


class Config:
    """a Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    DEBUG = True


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """
    Validate user login details
    Args:
        id (str): user id
    Returns:
        (Dict): user dictionary if id is valid else None
    """
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """
    Adds valid user to the global session object `g`
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@babel.localeselector
def get_locale() -> str:
    """
    For Getting locale from request object
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """default route"""
    return render_template("5-index.html",)


if __name__ == "__main__":
    app.run()
