#!/usr/bin/python3
"""Acessing Flask"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Renders state_list html pafe that displayes states"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontent
def teardown(self):
    """Method used to delete the SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
