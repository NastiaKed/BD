from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Library(db.Model):
    __tablename__ = 'Library'
    id: int = db.Column(db.Integer, primary_key=True)
    purchaseDate: db.Date = db.Column(db.Date)
    playtime: db.DateTime = db.Column(db.DateTime)
    user_UserID: int = db.Column(db.Integer, db.ForeignKey('user.id'))
    game_GameID: int = db.Column(db.Integer, db.ForeignKey('game.id'))
    Transaction_id: int = db.Column(db.Integer, db.ForeignKey('Transaction.id'))

    # game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    # user_id  = db.Column(db.Integer, db.ForeignKey('user.id'))

    # game = db.relationship('Game', back_populates='library')
    # Relationship 1:1 with Transaction
    # transaction = db.relationship('Transaction', back_populates='library')

    def __repr__(self) -> str:
        return (f"Library({self.id}, {self.purchaseDate}, {self.playtime}, {self.user_UserID}, "
                f"{self.game_GameID}, {self.Transaction_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        """
        return {
            "id": self.id,
            "purchaseDate": self.purchaseDate,
            "playtime": self.playtime,
            "user_UserID": self.user_UserID,
            "game_GameID": self.game_GameID,
            "Transaction_id": self.Transaction_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Library:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Library(
            purchaseDate=dto_dict.get("purchaseDate"),
            playtime=dto_dict.get("playtime"),
            user_UserID=dto_dict.get("user_UserID"),
            game_GameID=dto_dict.get("game_GameID"),
            Transaction_id=dto_dict.get("Transaction_id")
        )
        return obj
