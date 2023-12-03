from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import user_chat_controller
from t08_flask_mysql.app.my_project.auth.domain import UserChat

user_chat_bp = Blueprint('user_chats', __name__, url_prefix='/user_chats')


@user_chat_bp.get('')
def get_all_user_chats() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(user_chat_controller.find_all()), HTTPStatus.OK)


@user_chat_bp.post('')
def create_user_chat() -> Response:
    """
    Creates a user chat from the provided data.
    :return: Response object
    """
    content = request.get_json()
    user_chat = UserChat.create_from_dto(content)
    user_chat_controller.create(user_chat)
    return make_response(jsonify(user_chat.put_into_dto()), HTTPStatus.CREATED)


@user_chat_bp.get('/<int:user_chat_id>')
def get_user_chat(user_chat_id: int) -> Response:
    """
    Gets user chat by ID.
    :return: Response object
    """
    return make_response(jsonify(user_chat_controller.find_by_id(user_chat_id)), HTTPStatus.OK)


@user_chat_bp.put('/<int:user_chat_id>')
def update_user_chat(user_chat_id: int) -> Response:
    """
    Updates user chat by ID.
    :return: Response object
    """
    content = request.get_json()
    user_chat = UserChat.create_from_dto(content)
    user_chat_controller.update(user_chat_id, user_chat)
    return make_response("User chat updated", HTTPStatus.OK)


@user_chat_bp.patch('/<int:user_chat_id>')
def patch_user_chat(user_chat_id: int) -> Response:
    """
    Patches user chat by ID.
    :return: Response object
    """
    content = request.get_json()
    user_chat_controller.patch(user_chat_id, content)
    return make_response("User chat updated", HTTPStatus.OK)


@user_chat_bp.delete('/<int:user_chat_id>')
def delete_user_chat(user_chat_id: int) -> Response:
    """
    Deletes user chat by ID.
    :return: Response object
    """
    user_chat_controller.delete(user_chat_id)
    return make_response("User chat deleted", HTTPStatus.OK)
