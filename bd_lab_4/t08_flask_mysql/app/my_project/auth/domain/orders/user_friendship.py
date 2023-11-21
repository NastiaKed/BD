from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class UserFriendship(db.Model):
    __tablename__ = 'user_friendship'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'))
    user_2_id = db.Column(db.Integer, db.ForeignKey('user_2_id'))


    def __repr__(self) -> str:
        return f"UserFriendship({self.id}, {self.user_id}, {self.user_2_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user_2_id": self.user_2_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UserFriendship:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = UserFriendship(
            user_id=dto_dict.get("user_id"),
            user_2_id=dto_dict.get("user_2_id")
        )
        return obj