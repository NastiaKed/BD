# orders DB
from .orders.game_dao import GameDAO
from .orders.library_dao import LibraryDAO
from .orders.message_dao import MessageDAO
from .orders.review_dao import ReviewDAO
from .orders.transaction_dao import TransactionDAO
from .orders.user_dao import UserDAO
from .orders.user_chat_dao import UserChatDAO
from .orders.user_friendship_dao import UserFriendshipDAO
from .orders.favorite_game_dao import FavoriteGameDAO

game_dao = GameDAO()
library_dao = LibraryDAO()
message_dao = MessageDAO()
review_dao = ReviewDAO()
transaction_dao = TransactionDAO()
user_dao = UserDAO()
user_chat_dao = UserChatDAO()
user_friendship_dao = UserFriendshipDAO()
favorite_game_dao = FavoriteGameDAO()

