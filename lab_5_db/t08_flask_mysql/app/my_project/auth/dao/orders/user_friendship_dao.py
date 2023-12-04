from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import UserFriendship


class UserFriendshipDAO(GeneralDAO):
    _domain_type = UserFriendship

    def find_by_user_id(self, user_id: int) -> List[object]:
        return self._session.query(UserFriendship).filter(UserFriendship.user_id == user_id).all()

    def find_by_user_2_id(self, user_2_id: int) -> List[object]:
        return self._session.query(UserFriendship).filter(UserFriendship.user_2_id == user_2_id).all()

    def insert_user_friendship(self, id: int, user_id: int, user_2_id: int):
        try:
            self._session.execute(
                "CALL InsertIntoUserFriendship(:id, :user_id, :user_2_id)",
                {'id': id, 'user_id': user_id, 'user_2_id': user_2_id}
            )
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e

    def get_user_friendship_count(self) -> int:
        try:
            result = self._session.execute("SELECT GetUserFriendshipCount()").scalar()
            return result
        except Exception as e:
            raise e