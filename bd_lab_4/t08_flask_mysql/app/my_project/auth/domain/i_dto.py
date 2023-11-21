from abc import abstractmethod
from typing import Dict
from dataclasses import dataclass
from datetime import datetime


class IDto:
    """
    Interface to put and extract DTO objects to/from domain objects.
    """

    @abstractmethod
    def put_into_dto(self) -> Dict[str, object]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """

    @staticmethod
    @abstractmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """

@dataclass
class UserDto(IDto):
    """
    Data Transfer Object for User.
    """
    id: int
    user_name: str
    email: str
    password: str
    date_of_birth: datetime
    profile_picture: str
    user_friendship_id: int

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'UserDto':
        return UserDto(**dto_dict)

@dataclass
class GameDto(IDto):
    """
    Data Transfer Object for Game.
    """
    id: int
    title: str
    description: str
    release_date: datetime
    developer: str
    publisher: str
    genre: str
    price: float

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'GameDto':
        return GameDto(**dto_dict)

@dataclass
class TransactionDto(IDto):
    """
    Data Transfer Object for Transaction.
    """
    id: int
    amount: float
    timestamp: datetime

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'TransactionDto':
        return TransactionDto(**dto_dict)

@dataclass
class LibraryDto(IDto):
    """
    Data Transfer Object for Library.
    """
    id: int
    purchase_date: datetime
    playtime: datetime
    user_userid: int
    game_gameid: int
    transaction_id: int

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'LibraryDto':
        return LibraryDto(**dto_dict)

@dataclass
class ReviewDto(IDto):
    """
    Data Transfer Object for Review.
    """
    id: int
    rating: int
    review_text: str
    timestamp: datetime
    user_userid: int
    game_gameid: int

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'ReviewDto':
        return ReviewDto(**dto_dict)

@dataclass
class UserChatDto(IDto):
    """
    Data Transfer Object for User Chat.
    """
    user_userid: int
    id: int
    user_id: int

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'UserChatDto':
        return UserChatDto(**dto_dict)

@dataclass
class MessageDto(IDto):
    """
    Data Transfer Object for Message.
    """
    id: int
    content: str
    timestamp: datetime
    user_chat_id: int

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'MessageDto':
        return MessageDto(**dto_dict)

@dataclass
class UserFriendshipDto(IDto):
    """
    Data Transfer Object for User Friendship.
    """
    id: int
    user_id: int
    user_2_id: int

    def put_into_dto(self) -> Dict[str, object]:
        return self.__dict__

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'UserFriendshipDto':
        return UserFriendshipDto(**dto_dict)
