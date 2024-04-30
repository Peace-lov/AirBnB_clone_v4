#!/usr/bin/python3
"""Module holds the major application"""
from models import storage
from api.vI.views import app_views
from flask import Flask, make_response, jsonify
from os import getenv
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontent
def close_db(obj):
    """calls the mehtod close() on storage"""
    storage.close()


@app.erorhandle(404)
def page_not_found(error):
    """Looks for customised page not found"""
    return make_response(jsonify({"error": "Not found"}), 404)


app.config['SWAGGER'] = {
    'title': 'AirBnB clone - RESTful API',
    'description': 'This api was created to handle HBNB project,\
    Below are all the documentation',
    'universion': 3}

Swagger(app)

if __name__ == "__main__":

    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    app.run(host, int(port), threaded=True)
