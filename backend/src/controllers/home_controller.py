"""
Restful Api Actions for Home Page
"""

from src.models.architect import Architect
from flask import jsonify, request, Blueprint
from flasgger.utils import swag_from

# home controller blueprint to be registered with api blueprint
home_controller = Blueprint('/', __name__)


@home_controller.route('/', methods=['GET'], strict_slashes=False)
@swag_from('documentation/home/index.yml')
def home():
    architects = Architect.query.paginate(page=request.args.get('page', 1, type=int), per_page=5, error_out=False)
    list_architects = []
    for architect in architects:
        list_architects.append(architect.to_dict())
    return jsonify(list_architects)
