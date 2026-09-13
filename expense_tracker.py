# Python Expense Tracker - Version 2

expenses = []
categories = []

for i in range(3):
    print(f"\nExpense {i + 1}")
    category = input("Enter category (Food/Travel/Shopping): ")
    expense = float(input("Enter amount: ₹"))

    categories.append(category)
    expenses.append(expense)

total_expense = sum(expenses)
average_expense = total_expense / len(expenses)
highest_expense = max(expenses)
lowest_expense = min(expenses)

print("\n--- Expense Summary ---")

for i in range(len(expenses)):
    print(f"{categories[i]}: ₹{expenses[i]:.2f}")

print(f"\nTotal Expense: ₹{total_expense:.2f}")
print(f"Average Expense: ₹{average_expense:.2f}")
print(f"Highest Expense: ₹{highest_expense:.2f}")
print(f"Lowest Expense: ₹{lowest_expense:.2f}")
