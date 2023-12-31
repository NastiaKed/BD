from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Game(db.Model):
    __tablename__ = 'game'
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(80), index=True)
    description: str = db.Column(db.String(200))
    releaseDate: db.Date = db.Column(db.Date)
    developer: str = db.Column(db.String(100))
    publisher: str = db.Column(db.String(50))
    genre: str = db.Column(db.String(40))
    price: int = db.Column(db.Integer, index=True)

    def __repr__(self) -> str:
        return (
            f"Game({self.id}, '{self.title}', '{self.description}', {self.releaseDate}, "
            f"'{self.developer}', '{self.publisher}', '{self.genre}', {self.price})"
        )

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "releaseDate": self.releaseDate,
            "developer": self.developer,
            "publisher": self.publisher,
            "genre": self.genre,
            "price": self.price,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Game:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Game(
            title=dto_dict.get("title"),
            description=dto_dict.get("description"),
            releaseDate=dto_dict.get("releaseDate"),
            developer=dto_dict.get("developer"),
            publisher=dto_dict.get("publisher"),
            genre=dto_dict.get("genre"),
            price=dto_dict.get("price")
        )
        return obj
