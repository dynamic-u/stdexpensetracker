# transaction.py
# Defines the Transaction class
# Contributors: Implement attributes and methods for transaction details

'''
it is the sample code used for referance in future.
class Transaction:
    def __init__(self, amount, t_type, category, date, tid=None):
        """
        Initialize a transaction.
        :param amount: float - transaction amount
        :param t_type: str - 'income' or 'expense'
        :param category: str - category of transaction (e.g., food, salary)
        :param date: str - date in YYYY-MM-DD format
        :param tid: str - optional transaction ID
        """
        self.amount = amount
        self.t_type = t_type
        self.category = category
        self.date = date
        self.tid = tid if tid else f"{t_type}_{date}_{amount}"

    def __str__(self):
        """
        String representation for printing.
        Example: [expense] 2026-07-11 | Food | -500
        """
        sign = "-" if self.t_type == "expense" else "+"
        return f"[{self.t_type}] {self.date} | {self.category} | {sign}{self.amount}"


'''