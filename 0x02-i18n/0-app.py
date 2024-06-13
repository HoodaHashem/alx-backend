#!/usr/bin/env python3

""" Basic Babel setup """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Main route """
    return render_template('0-index.html')
