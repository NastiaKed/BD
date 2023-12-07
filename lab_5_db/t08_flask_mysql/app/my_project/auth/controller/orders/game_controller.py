from t08_flask_mysql.app.my_project.auth.service import game_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class GameController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = game_service

    def insert_game(self, title, description, release_date, developer, publisher, genre, price):
        result = self._service.insert_game(title, description, release_date, developer, publisher, genre, price)
        return result

    def get_game_count(self):
        result = self._service.get_game_count()
        return result

