#!/usr/bin/python3
"""Module holds the endpoint route"""
from models import storage
from flask import Flask
from api.v1.views import app_views
from flask import jsonify


@app_view.route('/status', strict_slashes=False)
def status():
    """Module returns a JSON status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def count():
    """Module returns no of each objects by type"""
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
