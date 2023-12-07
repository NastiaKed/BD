from t08_flask_mysql.app.my_project.auth.dao import review_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from sqlalchemy import text


class ReviewService(GeneralService):
    """
    Realisation of Library service.
    """
    _dao = review_dao

    def insert_into_review(self, user_userid: int, game_gameid: int, rating: int):
        result = self._dao.insert_game(user_userid, game_gameid, rating)
        return result
