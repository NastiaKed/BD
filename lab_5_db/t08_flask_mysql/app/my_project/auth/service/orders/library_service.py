from t08_flask_mysql.app.my_project.auth.dao import library_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

from typing import List
class LibraryService(GeneralService):
    """
    Realisation of Library service.
    """
    _dao = library_dao

    def find_libraries_by_user_id(self, user_id: int) -> List[object]:
        return self._dao.find_by_user_userid(user_id)