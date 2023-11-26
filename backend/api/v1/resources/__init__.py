"""
Blueprint for the api
"""
from flask import Blueprint

resources = Blueprint('resources', __name__, url_prefix='/api/v1')

from architects import *
from projects import *
