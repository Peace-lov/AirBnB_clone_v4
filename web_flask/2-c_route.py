#!/usr/bin/python3
"""Instiantiates an object from Flask"""
from flask import Flask
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


if __name__ == "__main__":
    """Hsst and port to be served"""
    app.run(host='0.0.0.0', port=5000)
