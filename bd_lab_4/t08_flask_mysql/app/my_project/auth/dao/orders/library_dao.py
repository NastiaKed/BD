from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Library


class LibraryDAO(GeneralDAO):
    _domain_type = Library

    def find_by_purchase_date(self, purchase_date: str) -> List[object]:
        return self._session.query(Library).filter(Library.purchase_date == purchase_date).order_by(Library.purchase_date).all()

    def find_by_playtime(self, playtime: str) -> List[object]:
        return self._session.query(Library).filter(Library.playtime == playtime).order_by(Library.playtime).all()

    def find_by_user_userid(self, user_userid: int) -> List[object]:
        return self._session.query(Library).filter(Library.user_UserID == user_userid).all()

    def find_by_game_gameid(self, game_gameid: int) -> List[object]:
        return self._session.query(Library).filter(Library.game_gameid == game_gameid).order_by(Library.game_gameid).all()

    def find_by_transaction_id(self, transaction_id: int) -> List[object]:
        return self._session.query(Library).filter(Library.transaction_id == transaction_id).order_by(Library.transaction_id).all()
