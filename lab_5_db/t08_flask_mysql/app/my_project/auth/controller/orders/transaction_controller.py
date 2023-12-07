from t08_flask_mysql.app.my_project.auth.service import transaction_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.dao.orders.transaction_dao import TransactionDAO
from sqlalchemy import text


class TransactionController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = transaction_service

    def insert_transaction_with_conversion_rate(self, id: int, amount: int, conversion_rate: float):
        try:
            self._service.insert_transaction_with_conversion_rate(id, amount, conversion_rate)
            return "Insert successful"
        except Exception as e:
            return f"Error: {str(e)}"

    def get_transaction_count(self) -> int:
        try:
            result = self._service.get_transaction_count()
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    def insert_transaction(self, id: int, amount: int):
        try:
            self._service.insert_transaction(id, amount)
            return "Insert successful"
        except Exception as e:
            return f"Error: {str(e)}"

