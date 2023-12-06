from flask import Blueprint
from src.controllers.auth_controller import user_controller
from src.controllers.architect_controller import architect_controller
from src.controllers.project_controller import project_controller

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(user_controller)
api.register_blueprint(architect_controller)
api.register_blueprint(project_controller)