from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import User


class UserDAO(GeneralDAO):
    _domain_type = User

    def find_by_first_name(self, first_name: str) -> List[object]:
        return self._session.query(User).filter(User.name == first_name).order_by(User.first_name).all()

    def find_by_last_name(self, last_name: str) -> List[object]:
        return self._session.query(User).filter(User.name == last_name).order_by(User.last_name).all()

    def find_by_email(self, email: str) -> List[object]:
        return self._session.query(User).filter(User.name == email).order_by(User.email).all()

    def insert_user(self, first_name: str, last_name: str, email: str) -> None:
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        self._session.add(new_user)
        self._session.commit()