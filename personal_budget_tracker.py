# CODE FOR BUDGET TRACKER
import json

class BudgetTracker:
    def __init__(self):
        self.balance = 0.0
        self.transactions = {'Income': [], 'Expenses': []}

    def add_income(self, amount, description):
        self.balance += amount
        self.transactions['Income'].append((amount, description))
        print(f"Income of ${amount} added. New balance: ${self.balance}")

    def add_expense(self, amount, category, description):
        self.balance -= amount
        self.transactions['Expenses'].append((amount, category, description))
        print(f"Expense of ${amount} under '{category}' added. New balance: ${self.balance}")

    def view_balance(self):
        print(f"Current Balance: ${self.balance}")

    def view_transactions(self):
        print("Transactions:")
        for category, transactions in self.transactions.items():
            print(f"{category}:")
            for transaction in transactions:
                amount, description = transaction[0], transaction[1]
                print(f"  - ${amount} - {description}")

    def save_data(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.transactions, f)
        print(f"Data saved to {filename}")

    def load_data(self, filename):
        try:
            with open(filename, 'r') as f:
                self.transactions = json.load(f)
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Save Data")
        print("6. Load Data")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            description = input("Enter description: ")
            budget_tracker.add_income(amount, description)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter description: ")
            budget_tracker.add_expense(amount, category, description)
        elif choice == '3':
            budget_tracker.view_balance()
        elif choice == '4':
            budget_tracker.view_transactions()
        elif choice == '5':
            filename = input("Enter filename to save (e.g., budget_data.json): ")
            budget_tracker.save_data(filename)
        elif choice == '6':
            filename = input("Enter filename to load (e.g., budget_data.json): ")
            budget_tracker.load_data(filename)
        elif choice == '7':
            print("Exiting the budget tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
