from t08_flask_mysql.app.my_project.auth.service import message_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class MessageController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = message_service
