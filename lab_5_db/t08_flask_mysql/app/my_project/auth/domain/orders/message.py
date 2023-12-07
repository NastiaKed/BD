from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime)
    user_chat_id = db.Column(db.Integer, db.ForeignKey('user_chat.id'))

    def __repr__(self) -> str:
        return f"Message({self.id}, '{self.content}', {self.timestamp}, {self.user_chat_id},)"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        """
        return {
            "id": self.id,
            "content": self.content,
            "timestamp": self.timestamp,
            "user_chat_id": self.user_chat_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Message:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Message(
            content=dto_dict.get("content"),
            timestamp=dto_dict.get("timestamp"),
            user_chat_id=dto_dict.get("user_chat_id"),
        )
        return obj