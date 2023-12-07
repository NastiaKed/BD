from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import UserFriendship


class UserFriendshipDAO(GeneralDAO):
    _domain_type = UserFriendship

    def find_by_user_id(self, user_id: int) -> List[object]:
        return self._session.query(UserFriendship).filter(UserFriendship.user_id == user_id).all()

    def find_by_user_2_id(self, user_2_id: int) -> List[object]:
        return self._session.query(UserFriendship).filter(UserFriendship.user_2_id == user_2_id).all()

    def insert_into_user_and_user_friendship(self, user_id: int, user_2_id: int):
        try:
            self._session.execute(
                "CALL InsertIntoUserAndUserFriendship(:user_id, :user_2_id)",
                {'user_id': user_id, 'user_2_id': user_2_id}
            )
            self._session.commit()
            return "Insert successful"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"