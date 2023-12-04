from .orders.game_controller import GameController
from .orders.library_controller import LibraryController
from .orders.message_controller import MessageController
from .orders.review_controller import ReviewController
from .orders.transaction_controller import TransactionController
from .orders.user_chat_controller import UserChatController
from .orders.user_controller import UserController
from .orders.user_friendship_controller import UserFriendshipController
from .orders.favorite_game_controller import FavoriteGameController



game_controller = GameController()
library_controller = LibraryController()
message_controller = MessageController()
review_controller = ReviewController()
transaction_controller = TransactionController()
user_chat_controller = UserChatController()
user_controller = UserController()
user_friendship_controller = UserFriendshipController()
favorite_game_controller = FavoriteGameController()
