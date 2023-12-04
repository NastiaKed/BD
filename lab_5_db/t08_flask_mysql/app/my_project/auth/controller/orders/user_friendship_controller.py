from t08_flask_mysql.app.my_project.auth.service import user_friendship_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.dao.orders.user_friendship_dao import UserFriendshipDAO


class UserFriendshipController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = user_friendship_service
    _dao = UserFriendshipDAO()

    def insert_user_friendship_with_stored_procedure(self, id: int, user_id: int, user_2_id: int):
        try:
            self._dao.insert_user_friendship(id, user_id, user_2_id)
            return {"message": "User friendship inserted successfully"}, 201
        except Exception as e:
            return {"error": str(e)}, 500
