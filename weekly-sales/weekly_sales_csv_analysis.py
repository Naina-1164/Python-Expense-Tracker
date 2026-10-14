"""Analyze weekly sales stored in a CSV file."""
import csv
from pathlib import Path

csv_path = Path(__file__).with_name("weekly_sales.csv")
total_sales = 0
days = 0
high_sales_days = 0

with csv_path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        sales = int(row["Sales"])
        total_sales += sales
        days += 1
        if sales >= 2000:
            high_sales_days += 1

if days == 0:
    print("No sales data found.")
else:
    print("WEEKLY SALES REPORT")
    print("-------------------")
    print("Total Sales:", total_sales)
    print("Average Sales:", total_sales / days)
    print("Days with sales >= 2000:", high_sales_days)
