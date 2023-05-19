#!/usr/bin/python3
"""
This is a Flask web application that displays routes.

Routes:
    - /: Didplays "Hello HBNB!"
    - /hbnb: Displays "HBNB"
    - /c/<text>: Display "C " followed by values of
    the text variables  (replace underscore with spaces)
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
