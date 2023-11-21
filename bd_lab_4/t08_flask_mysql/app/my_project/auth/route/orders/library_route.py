from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import library_controller
from t08_flask_mysql.app.my_project.auth.domain import Library

library_bp = Blueprint('libraries', __name__, url_prefix='/libraries')


@library_bp.get('')
def get_all_libraries() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(library_controller.find_all()), HTTPStatus.OK)


@library_bp.post('')
def create_library() -> Response:
    """
    Creates a library from the provided data.
    :return: Response object
    """
    content = request.get_json()
    library = Library.create_from_dto(content)
    library_controller.create(library)
    return make_response(jsonify(library.put_into_dto()), HTTPStatus.CREATED)


@library_bp.get('/<int:library_id>')
def get_library(library_id: int) -> Response:
    """
    Gets library by ID.
    :return: Response object
    """
    return make_response(jsonify(library_controller.find_by_id(library_id)), HTTPStatus.OK)


@library_bp.put('/<int:library_id>')
def update_library(library_id: int) -> Response:
    """
    Updates library by ID.
    :return: Response object
    """
    content = request.get_json()
    library = Library.create_from_dto(content)
    library_controller.update(library_id, library)
    return make_response("Library updated", HTTPStatus.OK)


@library_bp.patch('/<int:library_id>')
def patch_library(library_id: int) -> Response:
    """
    Patches library by ID.
    :return: Response object
    """
    content = request.get_json()
    library_controller.patch(library_id, content)
    return make_response("Library updated", HTTPStatus.OK)


@library_bp.delete('/<int:library_id>')
def delete_library(library_id: int) -> Response:
    """
    Deletes library by ID.
    :return: Response object
    """
    library_controller.delete(library_id)
    return make_response("Library deleted", HTTPStatus.OK)
