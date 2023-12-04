from typing import List

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

    def insert_review(self, rating: int, user_userid: int, game_gameid: int) -> None:
        new_review = Review(
            rating=rating,
            user_userid=user_userid,
            game_gameid=game_gameid
        )
        self._session.add(new_review)
        self._session.commit()