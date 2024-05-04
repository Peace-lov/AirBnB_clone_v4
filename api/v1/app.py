#!/usr/bin/python3
"""Module holds the flask application"""
from models import storage
from api.vI.views import app_views
from flask import Flask, make_response, jsonify, render_template
from os import environ
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
# cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ calls the mehtod close() on storage """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ Looks for customised page not found """
    return make_response(jsonify({"error": "Not found"}), 404)


app.config['SWAGGER'] = {
    'title': 'AirBnB clone - RESTful API',
    'universion': 3
}

Swagger(app)

if __name__ == "__main__":
    """ This is the main function """

    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
