from .orders.game_service import GameService
from .orders.library_service import LibraryService
from .orders.message_service import MessageService
from .orders.review_service import ReviewService
from .orders.transaction_service import TransactionService
from .orders.user_chat_service import UserChatService
from .orders.user_friendship_service import UserFriendshipService
from .orders.user_service import UserService
from .orders.favorite_game_service import FavoriteGameService



game_service = GameService()
library_service = LibraryService()
message_service = MessageService()
review_service = ReviewService()
transaction_service = TransactionService()
user_chat_service = UserChatService()
user_service = UserService()
user_friendship_service = UserFriendshipService()
favorite_game_service = FavoriteGameService()
