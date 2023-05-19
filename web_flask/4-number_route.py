#!/usr/bin/python3
"""
This is a Flask web application that displays various routes.

Routes:
    - /: Displays "Hello HBNB!"
    - /hbnb: Displays "HBNB"
    - /c/<text>: Displays "C " followed by the value of the
    text variable (replace underscores with spaces)
    - /python/(<text>): Displays "Python "
    followed by the value of the text
    variable (replace underscores with spaces)
    The default value of text is "is cool"
    - /number/<n>: Displays "n is a number" only if n is an integer
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace("__", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
