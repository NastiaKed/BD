from .orders.game_controller import GameController
from .orders.library_controller import LibraryController
from .orders.library_controller import MessageController
from .orders.library_controller import ReviewController
from .orders.library_controller import TransactionController
from .orders.library_controller import UserChatController
from .orders.library_controller import UserController
from .orders.library_controller import UserFriendshipController



game_controller = GameController()
library_controller = LibraryController()
message_controller = MessageController()
review_controller = ReviewController()
transaction_controller = TransactionController()
user_chat_controller = UserChatController()
user_controller = UserController()
user_friendship_controller = UserFriendshipController()
