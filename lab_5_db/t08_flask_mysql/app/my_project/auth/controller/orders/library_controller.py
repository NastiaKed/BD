from t08_flask_mysql.app.my_project.auth.service import library_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

from typing import List, Dict


class LibraryController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = library_service

    def find_libraries_by_user_id(self, user_id: int) -> List[Dict[str, object]]:
        """
        Finds libraries associated with a specific user by user_id.
        :param user_id: ID of the user
        :return: List of libraries associated with the user
        """
        return list(map(lambda x: x.put_into_dto(), self._service.find_libraries_by_user_id(user_id)))

    def create_tables(self):
        result = self._service.create_tables()
        return result