"""
Restful API for actions for projects
"""
from src import db
from src.models.architect import Architect
from src.models.project import Project
from flask import abort, jsonify, Blueprint, json
from flasgger.utils import swag_from

project_controller = Blueprint("projects", __name__)


@project_controller.route('/projects', methods=['GET'], strict_slashes=False)
@swag_from('documentation/project/index.yml')
def index():
    """
    Retrieves all projects
    :return:
    """
    projects = Project.query.all()
    project_data = []
    for project in projects:
        project_data.append(project.to_dict())
    return jsonify(project_data)


@project_controller.route('/projects/<project_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/project/show.yml')
def show(project_id):
    project = db.get(Project, project_id)
    if not project:
        abort(404)

    return jsonify(project.to_dict())


@project_controller.route('/architects/projects', methods=['GET'], strict_slashes=False)
@swag_from('documentation/project/architect_projects.yml')
def get_projects(architect_id):
    architect = Architect.query.get_or_404(architect_id)
    list_projects = []
    if not architect:
        abort(404)
    for project in architect.projects:
        list_projects.append(project.to_dict())

    return jsonify(list_projects)
