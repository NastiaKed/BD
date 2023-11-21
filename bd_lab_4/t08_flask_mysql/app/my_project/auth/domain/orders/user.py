from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(40), index=True)
    email = db.Column(db.String(20), index=True)
    password = db.Column(db.String(10))
    dateOfBirth = db.Column(db.Date)
    profilePicthure = db.Column(db.Integer)
    user_friendship_id = db.Column(db.Integer, nullable=False)

    # Relationship 1:M with Library
    library = db.relationship('Library', back_populates='user', cascade='all, delete-orphan')
    # Relationship 1:M with Review
    review = db.relationship('Review', back_populates='user', cascade='all, delete-orphan')
    # Relationship 1:M with UserChat
    user_chat = db.relationship('UserChat', back_populates='user', cascade='all, delete-orphan')
    # Relationship 1:M with UserFriendship
    user_friendship = db.relationship('UserFriendship', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self) -> str:
        return (f"User({self.id}, '{self.userName}', '{self.email}', '{self.password}')"
                f"{self.dateOfBirth}, {self.profilePicthure}, {self.user_friendship_id}")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        """
        return {
            "id": self.id,
            "userName": self.userName,
            "email": self.email,
            "password": self.password,
            "dateOfBirth": self.dateOfBirth,
            "profilePicture": self.profilePicthure,
            "user_friendship_id": self.user_friendship_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> User:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = User(
            userName=dto_dict.get("userName"),
            email=dto_dict.get("email"),
            password=dto_dict.get("password"),
            dateOfBirth=dto_dict.get("dateOfBirth"),
            profilePicture=dto_dict.get("profilePicture"),
            user_friendship_id=dto_dict.get("user_friendship_id")
        )
        return obj