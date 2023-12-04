from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Transaction


class TransactionDAO(GeneralDAO):
    _domain_type = Transaction

    def find_by_amount(self, amount: int) -> List[object]:
        return self._session.query(Transaction).filter(Transaction.amount == amount).all()

    def find_by_timestamp(self, timestamp: str) -> List[object]:
        return self._session.query(Transaction).filter(Transaction.timestamp == timestamp).all()

    def insert_transaction(self, amount: int, timestamp: str) -> None:
        new_transaction = Transaction(
            amount=amount,
            timestamp=timestamp
        )
        self._session.add(new_transaction)
        self._session.commit()