from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import favorite_game_controller
from t08_flask_mysql.app.my_project.auth.domain import FavoriteGame

favorite_game_bp = Blueprint('favorite_games', __name__, url_prefix='/favorite_games')


@favorite_game_bp.get('')
def get_all_favorite_games() -> Response:
    """
    Gets all favorite games using the service layer.
    :return: Response object
    """
    return make_response(jsonify(favorite_game_controller.find_all()), HTTPStatus.OK)


@favorite_game_bp.post('')
def create_favorite_game() -> Response:
    """
    Creates a favorite game from the provided data.
    :return: Response object
    """
    content = request.get_json()
    favorite_game = FavoriteGame.create_from_dto(content)
    favorite_game_controller.create(favorite_game)
    return make_response(jsonify(favorite_game.put_into_dto()), HTTPStatus.CREATED)


@favorite_game_bp.get('/<int:favorite_game_id>')
def get_favorite_game(favorite_game_id: int) -> Response:
    """
    Gets favorite game by ID.
    :return: Response object
    """
    return make_response(jsonify(favorite_game_controller.find_by_id(favorite_game_id)), HTTPStatus.OK)


@favorite_game_bp.put('/<int:favorite_game_id>')
def update_favorite_game(favorite_game_id: int) -> Response:
    """
    Updates favorite game by ID.
    :return: Response object
    """
    content = request.get_json()
    favorite_game = FavoriteGame.create_from_dto(content)
    favorite_game_controller.update(favorite_game_id, favorite_game)
    return make_response("Favorite game updated", HTTPStatus.OK)


@favorite_game_bp.patch('/<int:favorite_game_id>')
def patch_favorite_game(favorite_game_id: int) -> Response:
    """
    Patches favorite game by ID.
    :return: Response object
    """
    content = request.get_json()
    favorite_game_controller.patch(favorite_game_id, content)
    return make_response("Favorite game updated", HTTPStatus.OK)


@favorite_game_bp.delete('/<int:favorite_game_id>')
def delete_favorite_game(favorite_game_id: int) -> Response:
    """
    Deletes favorite game by ID.
    :return: Response object
    """
    favorite_game_controller.delete(favorite_game_id)
    return make_response("Favorite game deleted", HTTPStatus.OK)


