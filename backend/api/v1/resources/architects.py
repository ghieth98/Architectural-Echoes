"""
Restful API actions for architects
"""
from backend.api.v1.resources import resources
from flask import abort, jsonify
from flasgger.utils import swag_from


@resources.route('/architects', methods=['GET'], strict_slashes=False)
@swag_from('documentation/architect/index.yml')
def index():
    """
    Retrieves a list of all architects
    :return:
    """

    architects = db.all(Architect).values()
    list_architects = []
    for architect in architects:
        list_architects.append(architect.to_dict())
    return jsonify(list_architects)


@resources.route('/architects/<architect_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/architect/show.yml')
def show():
    """
    Retries an architect
    :return:
    """

    architect = db.get(Architect, architect_id)
    if not architect:
        abort(404)
    return jsonify(architect.to_dict())
