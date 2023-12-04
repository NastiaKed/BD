from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import UserChat


class UserChatDAO(GeneralDAO):

    _domain_type = UserChat

    def find_by_user_userid(self, user_userid: int) -> List[object]:
        return self._session.query(UserChat).filter(UserChat.user_userid == user_userid).all()

    def find_by_user_id(self, user_id: int) -> List[object]:
        return self._session.query(UserChat).filter(UserChat.user_id == user_id).all()

