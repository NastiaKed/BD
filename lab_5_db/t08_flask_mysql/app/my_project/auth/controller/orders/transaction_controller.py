from t08_flask_mysql.app.my_project.auth.service import transaction_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.dao.orders.transaction_dao import TransactionDAO


class TransactionController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = transaction_service
    _dao = TransactionDAO()

    def insert_transaction_with_stored_procedure(self, id: int, amount: int, conversion_rate: float):
        try:
            self._dao.insert_transaction_with_conversion_rate(id, amount, conversion_rate)
            return {"message": "Transaction inserted successfully"}, 201
        except Exception as e:
            return {"error": str(e)}, 500
