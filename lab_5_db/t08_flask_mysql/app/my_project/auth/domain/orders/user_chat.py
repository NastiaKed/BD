from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class UserChat(db.Model):
    __tablename__ = 'user_chat'
    user_UserID = db.Column(db.Integer, db.ForeignKey('user.id'))
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Relationship 1:M with Message
    # message = db.relationship('Message', back_populates='user_chat', cascade='all, delete-orphan')

    def __repr__(self) -> str:
        return f"UserChat({self.id}, {self.user_id}, {self.user_UserID})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user_UserID": self.user_UserID,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UserChat:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = UserChat(
            user_id=dto_dict.get("user_id"),
            user_UserID=dto_dict.get("user_UserID")
        )
        return obj