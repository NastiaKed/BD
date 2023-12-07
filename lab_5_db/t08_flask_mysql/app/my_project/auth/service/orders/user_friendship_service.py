from t08_flask_mysql.app.my_project.auth.dao import user_friendship_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class UserFriendshipService(GeneralService):
    """
    Realisation of Library service.
    """
    _dao = user_friendship_dao

    def insert_into_user_and_user_friendship(self, user_id: int, user_2_id: int):
        result = self._dao.insert_into_user_and_user_friendship(user_id, user_2_id)
        return result