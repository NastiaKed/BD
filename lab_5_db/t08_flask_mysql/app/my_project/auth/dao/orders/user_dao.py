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

    def insert_into_user(self, id: int, first_name: str, last_name: str, email: str, date_of_birth: str):
        try:
            self._session.execute(text("INSERT INTO user (id, first_name, last_name, email, date_of_birth) VALUES (:id, :first_name, :last_name, :email, :date_of_birth)"),
                                          {"id": id, "first_name": first_name, "last_name": last_name, "email": email, "date_of_birth": date_of_birth})
            self._session.commit()
            return "Insert successful"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"
