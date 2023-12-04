from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Message


class MessageDAO(GeneralDAO):
    _domain_type = Message

    def find_by_content(self, content: str) -> List[object]:
        return self._session.query(Message).filter(Message.content == content).all()

    def find_by_timestamp(self, timestamp: str) -> List[object]:
        return self._session.query(Message).filter(Message.timestamp == timestamp).all()

    def find_by_user_chat_id(self, user_chat_id: int) -> List[object]:
        return self._session.query(Message).filter(Message.user_chat_id == user_chat_id).all()

    def insert_message(self, content: str, timestamp: str, user_chat_id: int) -> None:
        new_message = Message(
            content=content,
            timestamp=timestamp,
            user_chat_id=user_chat_id
        )
        self._session.add(new_message)
        self._session.commit()