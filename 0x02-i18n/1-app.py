#!/usr/bin/env python3

""" Basic Babel setup """
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
babel = Babel(app)

@app.route('/')
def index():
    """ index route """
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')
