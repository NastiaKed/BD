from t08_flask_mysql.app.my_project.auth.service import user_friendship_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class UserFriendshipController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = user_friendship_service

    def insert_into_user_and_user_friendship(self, user_id: int, user_2_id: int):
        result = self._service.insert_into_user_and_user_friendship(user_id, user_2_id)
        return result
