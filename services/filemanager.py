# file_manager.py
# Handles saving/loading transactions from expenses.txt
# Contributors: Implement persistence functions

'''

it is the sample code used for referance in future.

import os
from models.transaction import Transaction

FILE_PATH = "expenses.txt"

def save_transaction(transaction):
    """
    Save a transaction to expenses.txt
    """
    with open(FILE_PATH, "a") as f:
        f.write(f"{transaction.tid},{transaction.amount},{transaction.t_type},{transaction.category},{transaction.date}\n")

def load_transactions():
    """
    Load all transactions from expenses.txt
    Returns a list of Transaction objects
    """
    transactions = []
    if not os.path.exists(FILE_PATH):
        return transactions

    with open(FILE_PATH, "r") as f:
        for line in f:
            tid, amount, t_type, category, date = line.strip().split(",")
            transactions.append(Transaction(float(amount), t_type, category, date, tid))
    return transactions

def delete_transaction(tid):
    """
    Delete a transaction by ID
    """
    transactions = load_transactions()
    transactions = [t for t in transactions if t.tid != tid]

    with open(FILE_PATH, "w") as f:
        for t in transactions:
            f.write(f"{t.tid},{t.amount},{t.t_type},{t.category},{t.date}\n")
    print("Transaction deleted successfully!")


'''