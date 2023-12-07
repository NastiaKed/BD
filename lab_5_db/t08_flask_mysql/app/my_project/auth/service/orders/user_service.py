from t08_flask_mysql.app.my_project.auth.dao import user_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from sqlalchemy import text


class UserService(GeneralService):
    """
    Realisation of Library service.
    """
    _dao = user_dao

    def insert_into_user(self, id: int, first_name: str, last_name: str, email: str, date_of_birth: str):
        result = self._dao.insert_into_user(id, first_name, last_name, email, date_of_birth)
        return result
