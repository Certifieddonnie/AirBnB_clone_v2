#!/usr/bin/python3
"""
A script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable
(replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text variable
(replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask, request, render_template
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
    return f"C {escape(text)}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyth(text="is cool"):
    """display “Python ”, followed by the value of the text variable
    with a defualt value of 'is cool'
    """
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer
    """
    if type(n) is int:
        return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n=None):
    """display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY"""
    if type(n) is int:
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
