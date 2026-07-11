# main.py
# Entry point for Personal Finance Tracker
# Provides a menu-driven console interface
# Contributors: Add new menu options here when extending functionality


'''
demo code content it is replacable in future.

 import sys
 from services.transaction_service import add_transaction, delete_transaction, view_transactions
 from services.summary_service import show_summary

 def main_menu():
     while True:
         print("\n=== Personal Finance Tracker ===")
         print("1. Add Transaction")
         print("2. Delete Transaction")
         print("3. View Transactions")
         print("4. Show Summary")
         print("5. Exit")

         choice = input("Enter your choice (1-5): ")

         try:
             if choice == "1":
                 add_transaction()   # Calls service to add a new transaction
             elif choice == "2":
                 delete_transaction() # Calls service to delete a transaction
            elif choice == "3":
                view_transactions()  # Displays all transactions
            elif choice == "4":
                show_summary()       # Shows totals and insights
            elif choice == "5":
                print("Exiting... Goodbye!")
                sys.exit()
            else:
                raise ValueError("Invalid menu option.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main_menu()

'''