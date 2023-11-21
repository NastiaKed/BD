from t08_flask_mysql.app.my_project.auth.service import library_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class LibraryController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = library_service
