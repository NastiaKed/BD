from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import user_friendship_controller
from t08_flask_mysql.app.my_project.auth.domain import UserFriendship

user_friendship_bp = Blueprint('user_friendships', __name__, url_prefix='/user_friendships')


@user_friendship_bp.get('')
def get_all_user_friendships() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(user_friendship_controller.find_all()), HTTPStatus.OK)


@user_friendship_bp.post('')
def create_user_friendship() -> Response:
    """
    Creates a user friendship from the provided data.
    :return: Response object
    """
    content = request.get_json()
    user_friendship = UserFriendship.create_from_dto(content)
    user_friendship_controller.create(user_friendship)
    return make_response(jsonify(user_friendship.put_into_dto()), HTTPStatus.CREATED)


@user_friendship_bp.get('/<int:user_friendship_id>')
def get_user_friendship(user_friendship_id: int) -> Response:
    """
    Gets user friendship by ID.
    :return: Response object
    """
    return make_response(jsonify(user_friendship_controller.find_by_id(user_friendship_id)), HTTPStatus.OK)


@user_friendship_bp.put('/<int:user_friendship_id>')
def update_user_friendship(user_friendship_id: int) -> Response:
    """
    Updates user friendship by ID.
    :return: Response object
    """
    content = request.get_json()
    user_friendship = UserFriendship.create_from_dto(content)
    user_friendship_controller.update(user_friendship_id, user_friendship)
    return make_response("User friendship updated", HTTPStatus.OK)


@user_friendship_bp.patch('/<int:user_friendship_id>')
def patch_user_friendship(user_friendship_id: int) -> Response:
    """
    Patches user friendship by ID.
    :return: Response object
    """
    content = request.get_json()
    user_friendship_controller.patch(user_friendship_id, content)
    return make_response("User friendship updated", HTTPStatus.OK)


@user_friendship_bp.delete('/<int:user_friendship_id>')
def delete_user_friendship(user_friendship_id: int) -> Response:
    """
    Deletes user friendship by ID.
    :return: Response object
    """
    user_friendship_controller.delete(user_friendship_id)
    return make_response("User friendship deleted", HTTPStatus.OK)
