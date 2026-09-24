# Python Expense Tracker - Version 4

import csv

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

# Save expenses to CSV
with open("expenses.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Amount"])

    for i in range(len(expenses)):
        writer.writerow([categories[i], expenses[i]])

print("\nExpenses saved to expenses.csv successfully.")

# Version 4: Read the saved CSV file
print("\n--- Saved Expenses ---")

with open("expenses.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        category = row[0]
        amount = float(row[1])
        print(f"{category}: ₹{amount:.2f}")
