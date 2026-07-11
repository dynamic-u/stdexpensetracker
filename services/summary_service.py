# summary_service.py
# Provides functions to show summaries and insights
# Contributors: Implement show_summary() to calculate totals and categories
''''

it is just a sample code used as referance for future.


import services.file_manager as fm
from models.budget import Budget

def show_summary():
    transactions = fm.load_transactions()
    budget = Budget(transactions)

    print("\n=== Summary ===")
    print(f"Total Income: {budget.total_income()}")
    print(f"Total Expense: {budget.total_expense()}")
    print(f"Balance: {budget.balance()}")


'''