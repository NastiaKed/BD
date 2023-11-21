from t08_flask_mysql.app.my_project.auth.dao import library_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class LibraryService(GeneralService):
    """
    Realisation of Library service.
    """
    _dao = library_dao
