from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Library(db.Model):
    __tablename__ = 'library'
    id = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.Date)
    playtime = db.Column(db.DateTime)
    user_userid = db.Column(db.Integer, nullable=False)
    game_gameid = db.Column(db.Integer, nullable=False, index=True)
    transaction_id = db.Column(db.Integer, nullable=False)

    # Relationship 1:1 with Transaction
    transaction = db.relationship('Transaction', back_populates='library')

    def __repr__(self) -> str:
        return (f"Library({self.id}, {self.purchase_date}, {self.playtime}, {self.user_userid},)"
                f"'{self.game_gameid}, {self.transaction_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        """
        return {
            "id": self.id,
            "purchase_date": self.purchase_date,
            "playtime": self.playtime,
            "user_userid": self.user_userid,
            "game_gameid": self.game_gameid,
            "transaction_id": self.transaction_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Library:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Library(
            purchase_date=dto_dict.get("purchase_date"),
            playtime=dto_dict.get("playtime"),
            user_userid=dto_dict.get("user_userid"),
            game_gameid=dto_dict.get("game_gameid"),
            transaction_id=dto_dict.get("transaction_id")
        )
        return obj