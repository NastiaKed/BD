from t08_flask_mysql.app.my_project.auth.service import game_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class GameController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = game_service
