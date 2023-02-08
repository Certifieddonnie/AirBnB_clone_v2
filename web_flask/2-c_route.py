#!/usr/bin/python3
"""
A script that starts a Flask web application:
"""

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns a string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello2():
    """Returns another string"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text=None):
    """display “C ” followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
