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


if __name__ == "__main__":
    """Hsst and port to be served"""
    app.run(host='0.0.0.0', port=5000)
