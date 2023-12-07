from t08_flask_mysql.app.my_project.auth.service import user_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from sqlalchemy import text


class UserController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = user_service

    def insert_into_user(self, id: int, first_name: str, last_name: str, email: str, date_of_birth: str):
        result = self._service.insert_into_user(id, first_name, last_name, email, date_of_birth)
        return result
