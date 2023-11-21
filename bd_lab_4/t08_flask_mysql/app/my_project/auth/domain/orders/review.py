from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    review_text = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime)
    user_userid = db.Column(db.Integer, db.ForeignKey('user_userid'))
    game_gameid = db.Column(db.Integer, db.ForeignKey('game_gameid'))


    def __repr__(self) -> str:
        return (f"Game({self.id}, {self.rating}, '{self.review_text}', {self.timestamp})"
                f"{self.user_userid}, {self.game_gameid})")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        """
        return {
            "id": self.id,
            "rating": self.rating,
            "review_text": self.review_text,
            "timestamp": self.timestamp,
            "user_userid": self.user_userid,
            "game_gameid": self.game_gameid,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Review:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Review(
            rating=dto_dict.get("rating"),
            review_text=dto_dict.get("review_text"),
            timestamp=dto_dict.get("timestamp"),
            user_userid=dto_dict.get("user_userid"),
            game_gameid=dto_dict.get("game_gameid")
        )
        return obj