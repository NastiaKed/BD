from t08_flask_mysql.app.my_project.auth.service import game_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.dao.orders.game_dao import GameDAO

class GameController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = game_service
    _dao = GameDAO()

    def insert_game_with_stored_procedure(self, id: int, title: str, description: str, release_date: str,
                                          developer: str, publisher: str, genre: str, price: int):
        try:
            self._dao.insert_game(id, title, description, release_date, developer, publisher, genre, price)
            return {"message": "Game inserted successfully"}, 201
        except Exception as e:
            return {"error": str(e)}, 500
