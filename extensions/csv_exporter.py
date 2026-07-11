# csv_exporter.py
# Future: Export transactions to CSV for Excel integration
# Contributors: Implement export_to_csv()
'''
it is the sample code used for referance in future.

import csv
import services.file_manager as fm

def export_to_csv(filename="expenses.csv"):
    transactions = fm.load_transactions()
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Amount", "Type", "Category", "Date"])
        for t in transactions:
            writer.writerow([t.tid, t.amount, t.t_type, t.category, t.date])
    print(f"Transactions exported to {filename}")
'''