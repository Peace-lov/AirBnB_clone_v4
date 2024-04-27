#!/usr/bin/python3
"""Instiantiates an object from Flask"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Responds wit the messge when / is requested"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Responds with a mesage below when /hbnb is requested"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Responds with a message when /c is called"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def python_is_ccol(text='is_cool'):
    """Responds with a message when /python is called"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_n_number(n):
    """Responds with a message when /number is called"""
    return '{:d} is a number'.format(n)


if __name__ == "__main__":
    """Hsst and port to be served"""
    app.run(host='0.0.0.0', port=5000)
