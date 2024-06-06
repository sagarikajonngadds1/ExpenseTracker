import json
from datetime import datetime

# Define the path to the JSON file for data storage
DATA_FILE = 'expenses.json'

# Function to load expenses from the JSON file
def load_expenses():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save expenses to the JSON file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Function to add a new expense
def add_expense(amount, description, category):
    expenses = load_expenses()
    expense = {
        'amount': amount,
        'description': description,
        'category': category,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    expenses.append(expense)
    save_expenses(expenses)

# Function to get user input and add an expense
def input_expense():
    try:
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        category = input("Enter the category: ")
        add_expense(amount, description, category)
        print("Expense added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

# Function to view all expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return

    for expense in expenses:
        print(f"Amount: {expense['amount']}, Description: {expense['description']}, "
              f"Category: {expense['category']}, Date: {expense['date']}")

# Function to analyze expenses by category and month
def analyze_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return

    category_totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\nExpense Analysis by Category:")
    for category, total in category_totals.items():
        print(f"{category}: {total}")

    monthly_totals = {}
    for expense in expenses:
        date = datetime.strptime(expense['date'], '%Y-%m-%d %H:%M:%S')
        month = date.strftime('%Y-%m')
        amount = expense['amount']
        if month in monthly_totals:
            monthly_totals[month] += amount
        else:
            monthly_totals[month] = amount

    print("\nMonthly Expense Summary:")
    for month, total in monthly_totals.items():
        print(f"{month}: {total}")

# Main function to run the expense tracker
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            input_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            analyze_expenses()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()