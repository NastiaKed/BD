# dto.py

from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserDto:
    id: int
    user_name: str
    email: str
    password: str
    date_of_birth: datetime
    profile_picture: str
    user_friendship_id: int

@dataclass
class GameDto:
    id: int
    title: str
    description: str
    release_date: datetime
    developer: str
    publisher: str
    genre: str
    price: float

@dataclass
class TransactionDto:
    id: int
    amount: float
    timestamp: datetime
    
@dataclass
class LibraryDto:
    id: int
    purchase_date: datetime
    playtime: datetime
    user_UserID: int
    game_GameID: int
    Transaction_id: int

@dataclass
class ReviewDto:
    id: int
    rating: int
    reviewText: str
    timestamp: datatime
