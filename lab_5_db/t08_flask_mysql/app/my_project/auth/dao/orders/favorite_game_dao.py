from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.favorite_game import FavoriteGame


class FavoriteGameDAO(GeneralDAO):
    _domain_type = FavoriteGame

    def find_by_game_id(self, game_id: int) -> List[object]:
        return self._session.query(FavoriteGame).filter(FavoriteGame.game_id == game_id).order_by(FavoriteGame.game_id).all()

    def find_by_game_name(self, game_name: str) -> List[object]:
        return self._session.query(FavoriteGame).filter(FavoriteGame.game_name == game_name).order_by(FavoriteGame.game_name).all()

    def find_by_user_id(self, user_id: int) -> List[object]:
        return self._session.query(FavoriteGame).filter(FavoriteGame.user_id == user_id).order_by(FavoriteGame.user_id).all()
