from t08_flask_mysql.app.my_project.auth.dao import transaction_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class TransactionService(GeneralService):
    """
    Realisation of Library service.
    """
    _dao = transaction_dao

    def insert_transaction_with_conversion_rate(self, id: int, amount: int, conversion_rate: float):
        try:
            self._dao.insert_transaction_with_conversion_rate(id, amount, conversion_rate)
            return "Insert successful"
        except Exception as e:
            return f"Error: {str(e)}"

    def get_transaction_count(self) -> int:
        try:
            result = self._dao.get_transaction_count()
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    def insert_transaction(self, id: int, amount: int):
        try:
            self._dao.insert_transaction(id, amount)
            return "Insert successful"
        except Exception as e:
            return f"Error: {str(e)}"