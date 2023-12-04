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

    def insert_game(self, id: int, title: str, description: str, release_date: str, developer: str,
                    publisher: str, genre: str, price: int):
        try:
            self._session.execute(
                "CALL InsertIntoGame(:id, :title, :description, :release_date, :developer, :publisher, :genre, :price)",
                {'id': id, 'title': title, 'description': description, 'release_date': release_date,
                 'developer': developer, 'publisher': publisher, 'genre': genre, 'price': price}
            )
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e

    def get_game_count(self) -> int:
        try:
            result = self._session.execute("SELECT GetGameCount()").scalar()
            return result
        except Exception as e:
            raise e