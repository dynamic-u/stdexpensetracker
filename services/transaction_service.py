# transaction_service.py
# Provides functions for adding, deleting, and viewing transactions
# Contributors: Connects user input to Transaction objects and file_manager
'''

it is the sample code used for referance in future.


from models.transaction import Transaction
import services.file_manager as fm

def add_transaction():
    try:
        amount = float(input("Enter amount: "))
        t_type = input("Enter type (income/expense): ").lower()
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")

        transaction = Transaction(amount, t_type, category, date)
        fm.save_transaction(transaction)
        print("Transaction added successfully!")
    except ValueError:
        print("Invalid input. Amount must be a number.")

def delete_transaction():
    tid = input("Enter transaction ID to delete: ")
    fm.delete_transaction(tid)

def view_transactions():
    transactions = fm.load_transactions()
    if not transactions:
        print("No transactions found.")
    for t in transactions:
        print(t)

'''