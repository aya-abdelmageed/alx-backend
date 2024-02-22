#!/usr/bin/env python3
"""task 3"""
from flask import Flask, render_template, request
from flask_babel import Babel


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


@babel.localeselector
def get_locale() -> str:
    """
    For Getting locale from request object
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """default route"""
    return render_template("3-index.html",)


if __name__ == "__main__":
    app.run()
