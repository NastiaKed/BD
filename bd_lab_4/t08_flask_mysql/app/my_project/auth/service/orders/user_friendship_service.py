from t08_flask_mysql.app.my_project.auth.dao import user_friendship_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class UserFriendshipService(GeneralService):
    """
    Realisation of Library service.
    """
    _dao = user_friendship_dao