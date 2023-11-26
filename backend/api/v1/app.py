from flask import Flask, make_response, jsonify, render_template
from resources import resources
from os import environ
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(resources)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

app.errorhandler(404)


def not_found(error):
    """404 Error not found"""
    return make_response(jsonify({'error': 'Not Found'}), 404)


app.config['SWAGGER'] = {
    'title': 'Architectural Echoes',
    'universion': 3
}

Swagger(app)

if __name__ == '__main__':
    app.run(debug=True)
