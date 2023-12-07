from typing import List
from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Review


class ReviewDAO(GeneralDAO):
    _domain_type = Review

    def find_by_rating(self, rating: int) -> List[object]:
        return self._session.query(Review).filter(Review.rating == rating).all()

    def find_by_user_userid(self, user_userid: int) -> List[object]:
        return self._session.query(Review).filter(Review.user_userid == user_userid).all()

    def find_by_game_gameid(self, game_gameid: int) -> List[object]:
        return self._session.query(Review).filter(Review.game_gameid == game_gameid).all()

    def insert_into_review(self, user_userid: int, game_gameid: int, rating: int):
        try:
            self._session.execute(text("INSERT INTO review (user_userid, game_gameid, rating) VALUES (:user_userid, :game_gameid, :rating)"),
                                          {"user_userid": user_userid, "game_gameid": game_gameid, "rating": rating})
            self._session.commit()
            return "Insert successful"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"