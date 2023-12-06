"""
Restful API actions for architects
"""
from urllib import response

from src import db
from src.models.architect import Architect
from flask import abort, jsonify, Blueprint, Response, json
from flasgger.utils import swag_from

# architect controller blueprint to be registered with api blueprint
architect_controller = Blueprint("architects", __name__)


@architect_controller.route('/architects', methods=['GET'], strict_slashes=False)
@swag_from('documentation/architect/index.yml')
def index():
    """
    Retrieves a list of all architects
    :return:
    """

    architects = Architect.query.all()
    list_architects = []
    for architect in architects:
        list_architects.append(architect.to_dict())
    return jsonify(list_architects)



@architect_controller.route('/architects/<architect_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/architect/show.yml')
def show(architect_id):
    """
    Retries an architect
    :return:
    """

    architect = Architect.query.get_or_404(architect_id)
    return jsonify(architect.to_dict())
