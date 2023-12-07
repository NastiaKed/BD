from t08_flask_mysql.app.my_project.auth.dao import favorite_game_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class FavoriteGameService(GeneralService):
    """
    Realisation of Favorite Game service
    """
    _dao = favorite_game_dao
