from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, index=True)
    timestamp = db.Column(db.DateTime)


    def __repr__(self) -> str:
        return f"Transaction({self.id}, {self.amount}, {self.timestamp})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        """
        return {
            "id": self.id,
            "amount": self.amount,
            "timestamp": self.timestamp,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Transaction:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Transaction(
            amount=dto_dict.get("amount"),
            timestamp=dto_dict.get("timestamp")
        )
        return obj