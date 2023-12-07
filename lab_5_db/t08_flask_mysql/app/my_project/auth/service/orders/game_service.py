from t08_flask_mysql.app.my_project.auth.dao import game_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from sqlalchemy import text


class GameService(GeneralService):
    """
    Realisation of Game service.
    """
    _dao = game_dao

    def insert_game(self, title, description, release_date, developer, publisher, genre, price):
        result = self._dao.insert_game(title, description, release_date, developer, publisher, genre, price)
        return result

    def get_game_count(self):
        result = self._dao.get_game_count()
        return result
