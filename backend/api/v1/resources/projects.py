"""
Restful API for actions for projects
"""

from backend.api.v1.resources import resources
from flask import abort, jsonify
from flasgger.utils import swag_from


@resources.route('/projects', methods=['GET'], strict_slashes=False)
@swag_from('documentation/project/index.yml')
def index():
    """
    Retrieves all projects
    :return:
    """
    projects = db.all(Project).values()
    list_of_projects = []
    for project in projects:
        list_of_projects.append(project.to_dict())

    return jsonify(list_of_projects)


@resources.route('/projects/<project_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/project/show.yml')
def show():
    project = db.get(Project, project_id)
    if not project:
        abort(404)

    return jsonify(project.to_dict())

@resources.route('/architects/projects', methods=['GET'], strict_slashes=False)
@swag_from('documentation/project/architect_projects.yml')
def get_projects():
    architect = db.get(Architect, architect_id)
    list_projects = []
    if not architect:
        abort(404)
    for project in architect.projects:
        list_projects.append(project.to_dict())

    return jsonify(list_projects)


