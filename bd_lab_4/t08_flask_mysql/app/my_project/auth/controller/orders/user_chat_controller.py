from t08_flask_mysql.app.my_project.auth.service import user_chat_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class UserChatController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = user_chat_service
