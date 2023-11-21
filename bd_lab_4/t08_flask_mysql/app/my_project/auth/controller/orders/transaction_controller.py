from t08_flask_mysql.app.my_project.auth.service import transaction_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class TransactionController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = transaction_service
