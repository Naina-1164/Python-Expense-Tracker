# Python Expense Tracker - Version 1

expenses = []

for i in range(3):
    expense = float(input(f"Enter expense {i + 1}: ₹"))
    expenses.append(expense)

total_expense = sum(expenses)
average_expense = total_expense / len(expenses)

print("\n--- Expense Summary ---")
print("Your Expenses:", expenses)
print(f"Total Expense: ₹{total_expense:.2f}")
print(f"Average Expense: ₹{average_expense:.2f}")
