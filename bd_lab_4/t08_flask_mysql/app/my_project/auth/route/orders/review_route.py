from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import review_controller
from t08_flask_mysql.app.my_project.auth.domain import Review

review_bp = Blueprint('reviews', __name__, url_prefix='/reviews')


@review_bp.get('')
def get_all_reviews() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(review_controller.find_all()), HTTPStatus.OK)


@review_bp.post('')
def create_review() -> Response:
    """
    Creates a review from the provided data.
    :return: Response object
    """
    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.create(review)
    return make_response(jsonify(review.put_into_dto()), HTTPStatus.CREATED)


@review_bp.get('/<int:review_id>')
def get_review(review_id: int) -> Response:
    """
    Gets review by ID.
    :return: Response object
    """
    return make_response(jsonify(review_controller.find_by_id(review_id)), HTTPStatus.OK)


@review_bp.put('/<int:review_id>')
def update_review(review_id: int) -> Response:
    """
    Updates review by ID.
    :return: Response object
    """
    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.update(review_id, review)
    return make_response("Review updated", HTTPStatus.OK)


@review_bp.patch('/<int:review_id>')
def patch_review(review_id: int) -> Response:
    """
    Patches review by ID.
    :return: Response object
    """
    content = request.get_json()
    review_controller.patch(review_id, content)
    return make_response("Review updated", HTTPStatus.OK)


@review_bp.delete('/<int:review_id>')
def delete_review(review_id: int) -> Response:
    """
    Deletes review by ID.
    :return: Response object
    """
    review_controller.delete(review_id)
    return make_response("Review deleted", HTTPStatus.OK)
