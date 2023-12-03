from t08_flask_mysql.app.my_project.auth.dao import game_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class GameService(GeneralService):
    """
    Realisation of Game service.
    """
    _dao = game_dao
