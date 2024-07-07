import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, data_file='expenses.json'):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        try:
            amount = float(amount)
            expense = {
                'amount': amount,
                'category': category,
                'description': description,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            self.expenses.append(expense)
            self.save_data()
            print("Expense added successfully.")
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")

    def monthly_summary(self):
        summary = {}
        for expense in self.expenses:
            month = expense['date'][:7]  # Extract the month in 'YYYY-MM' format
            if month not in summary:
                summary[month] = 0
            summary[month] += expense['amount']

        for month, total in summary.items():
            print(f"Month: {month}, Total Expenses: {total}")

    def category_summary(self):
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            if category not in summary:
                summary[category] = 0
            summary[category] += expense['amount']

        for category, total in summary.items():
            print(f"Category: {category}, Total Expenses: {total}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.monthly_summary()
        elif choice == '4':
            tracker.category_summary()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
