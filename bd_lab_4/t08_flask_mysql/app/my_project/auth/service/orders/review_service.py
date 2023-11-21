from t08_flask_mysql.app.my_project.auth.dao import review_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ReviewService(GeneralService):
    """
    Realisation of Library service.
    """
    _dao = review_dao