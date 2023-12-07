from typing import List
from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Transaction


class TransactionDAO(GeneralDAO):
    _domain_type = Transaction

    def find_by_amount(self, amount: int) -> List[object]:
        return self._session.query(Transaction).filter(Transaction.amount == amount).all()

    def find_by_timestamp(self, timestamp: str) -> List[object]:
        return self._session.query(Transaction).filter(Transaction.timestamp == timestamp).all()

    def insert_transaction_with_conversion_rate(self, id: int, amount: int, conversion_rate: float):
        try:
            self._session.execute(
                "CALL InsertIntoTransactionWithConversionRate(:id, :amount, :conversion_rate)",
                {'id': id, 'amount': amount, 'conversion_rate': conversion_rate}
            )
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e

    def get_transaction_count(self) -> int:
        try:
            result = self._session.execute("SELECT GetTransactionCount()").scalar()
            return result
        except Exception as e:
            raise e

    def insert_transaction(self, id: int, amount: int):
        try:
            self._session.execute(text("INSERT INTO transaction (id, amount) VALUES (:id, :amount)"),
                                  {"id": id, "amount": amount})
            self._session.commit()
            return "Insert successful"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"
