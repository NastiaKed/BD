from t08_flask_mysql.app.my_project.auth.service import review_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ReviewController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = review_service

    def insert_into_review(self, user_userid: int, game_gameid: int, rating: int):
        result = self._service.insert_game(user_userid, game_gameid, rating)
        return result
