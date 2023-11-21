from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)

    from .orders.user_route import user_bp
    from .orders.game_route import game_bp
    from .orders.message_route import message_bp
    from .orders.review_route import review_bp
    from .orders.transaction_route import transaction_bp
    from .orders.user_chat_route import user_chat_bp
    from .orders.user_friendship_route import user_friendship_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(game_bp)
    app.register_blueprint(message_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(user_chat_bp)
    app.register_blueprint(user_friendship_bp)
