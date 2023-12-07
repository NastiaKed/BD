from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db


class FavoriteGame(db.Model):
    __tablename__ = 'favorite_game'
    game_id: int = db.Column(db.Integer, primary_key=True)
    game_name: str = db.Column(db.String(50))
    user_id: int = db.Column(db.Integer)

    def __repr__(self) -> str:
        return (
            f"Favorite Game({self.game_id}, '{self.game_name}', {self.user_id})"
        )


    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        """
        return {
            "game_id": self.game_id,
            "game_name": self.game_name,
            "user_id": self.user_id,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> FavoriteGame:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = FavoriteGame(
            game_name=dto_dict.get("game_name")
        )
        return obj