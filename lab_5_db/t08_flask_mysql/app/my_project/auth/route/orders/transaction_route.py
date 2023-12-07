from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import transaction_controller
from t08_flask_mysql.app.my_project.auth.domain import Transaction

transaction_bp = Blueprint('transactions', __name__, url_prefix='/transactions')


@transaction_bp.get('')
def get_all_transactions() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(transaction_controller.find_all()), HTTPStatus.OK)


@transaction_bp.post('')
def create_transaction() -> Response:
    """
    Creates a transaction from the provided data.
    :return: Response object
    """
    content = request.get_json()
    transaction = Transaction.create_from_dto(content)
    transaction_controller.create(transaction)
    return make_response(jsonify(transaction.put_into_dto()), HTTPStatus.CREATED)


@transaction_bp.get('/<int:transaction_id>')
def get_transaction(transaction_id: int) -> Response:
    """
    Gets transaction by ID.
    :return: Response object
    """
    return make_response(jsonify(transaction_controller.find_by_id(transaction_id)), HTTPStatus.OK)


@transaction_bp.put('/<int:transaction_id>')
def update_transaction(transaction_id: int) -> Response:
    """
    Updates transaction by ID.
    :return: Response object
    """
    content = request.get_json()
    transaction = Transaction.create_from_dto(content)
    transaction_controller.update(transaction_id, transaction)
    return make_response("Transaction updated", HTTPStatus.OK)


@transaction_bp.patch('/<int:transaction_id>')
def patch_transaction(transaction_id: int) -> Response:
    """
    Patches transaction by ID.
    :return: Response object
    """
    content = request.get_json()
    transaction_controller.patch(transaction_id, content)
    return make_response("Transaction updated", HTTPStatus.OK)


@transaction_bp.delete('/<int:transaction_id>')
def delete_transaction(transaction_id: int) -> Response:
    """
    Deletes transaction by ID.
    :return: Response object
    """
    transaction_controller.delete(transaction_id)
    return make_response("Transaction deleted", HTTPStatus.OK)


@transaction_bp.post('/conversion')
def create_transaction_with_conversion() -> Response:
    """
    Creates a transaction with a conversion rate from the provided data.
    :return: Response object
    """
    content = request.get_json()
    id = content.get('id')
    amount = content.get('amount')
    conversion_rate = content.get('conversion_rate')
    transaction_controller.insert_transaction_with_conversion_rate(id, amount, conversion_rate)
    return make_response("Transaction with conversion rate created", HTTPStatus.CREATED)

