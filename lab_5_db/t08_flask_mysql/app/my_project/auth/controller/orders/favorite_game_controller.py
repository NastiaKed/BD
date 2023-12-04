from t08_flask_mysql.app.my_project.auth.service import favorite_game_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class FavoriteGameController(GeneralController):
    """
    Realisation of Favorite Game controller.
    """
    _service = favorite_game_service
