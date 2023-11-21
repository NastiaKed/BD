from t08_flask_mysql.app.my_project.auth.service import review_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ReviewController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = review_service
