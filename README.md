# Python Expense Tracker

A beginner-friendly Python project that I am improving step by step while practicing programming fundamentals.

## Version 3 - Save Expenses to CSV

The program asks the user to enter 3 expenses with categories. It displays a simple expense summary and now also saves the entered data to an `expenses.csv` file.

### Current Features

- Enter 3 expenses and categories
- Display each expense with its category
- Calculate total expense
- Calculate average expense
- Find highest and lowest expense
- Save category and amount data to CSV

## Concepts Practiced

- `input()`
- Lists and `for` loops
- `sum()`, `max()`, and `min()`
- Basic calculations
- Python `csv` module
- `with open()`
- `csv.writer()`
- Writing rows to a file

## How to Run

```bash
python expense_tracker.py
```

After entering the expenses, the program creates `expenses.csv` in the same folder.

Example:

```csv
Category,Amount
Food,250
Travel,500
Shopping,300
```

## Learning Progress

**Version 1:** Entered 3 expenses and calculated total and average.

**Version 2:** Added expense categories and highest/lowest expense calculations.

**Version 3:** Added basic CSV file saving using Python's built-in `csv` module.

The project is intentionally improving gradually. Pandas and more advanced data analysis can be introduced in a later version.
