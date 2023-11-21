from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Game


class GameDAO(GeneralDAO):
    _domain_type = Game

    def find_by_title(self, title: str) -> List[object]:
        return self._session.query(Game).filter(Game.title == title).order_by(Game.title).all()

    def find_by_release_date(self, release_date: str) -> List[object]:
        return self._session.query(Game).filter(Game.release_date == release_date).order_by(Game.release_date).all()

    def find_by_developer(self, developer: str) -> List[object]:
        return self._session.query(Game).filter(Game.developer == developer).order_by(Game.developer).all()

    def find_by_genre(self, genre: str) -> List[object]:
        return self._session.query(Game).filter(Game.genre == genre).order_by(Game.genre).all()
