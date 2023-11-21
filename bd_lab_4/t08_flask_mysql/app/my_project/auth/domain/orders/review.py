from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Review(db.Model):
    __tablename__ = 'Review'
    id: int = db.Column(db.Integer, primary_key=True)
    rating: int = db.Column(db.Integer)
    reviewText: str = db.Column(db.String(100))
    timestamp: db.DateTime = db.Column(db.DateTime)
    user_UserID: int = db.Column(db.Integer, db.ForeignKey('user.id'))
    game_GameID: int = db.Column(db.Integer, db.ForeignKey('game.id'))

    # # Relationship M:1 with Game
    # game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    # game = db.relationship('Game', back_populates='review')

    def __repr__(self) -> str:
        return (f"Review({self.id}, {self.rating}, '{self.reviewText}', {self.timestamp}, "
                f"{self.user_UserID}, {self.game_GameID})")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        """
        return {
            "id": self.id,
            "rating": self.rating,
            "reviewText": self.reviewText,
            "timestamp": self.timestamp,
            "user_UserID": self.user_UserID,
            "game_GameID": self.game_GameID,
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
            reviewText=dto_dict.get("reviewText"),
            timestamp=dto_dict.get("timestamp"),
            user_UserID=dto_dict.get("user_UserID"),
            game_GameID=dto_dict.get("game_GameID")
        )
        return obj
