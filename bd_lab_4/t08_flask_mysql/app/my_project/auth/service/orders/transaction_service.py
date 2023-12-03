from t08_flask_mysql.app.my_project.auth.dao import transaction_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class TransactionService(GeneralService):
    """
    Realisation of Library service.
    """
    _dao = transaction_dao