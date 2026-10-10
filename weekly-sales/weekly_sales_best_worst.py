"""Find best and worst sales days using beginner-friendly loops."""

sales = {
    "Monday": 1200,
    "Tuesday": 1500,
    "Wednesday": 1100,
    "Thursday": 1800,
    "Friday": 2100,
    "Saturday": 2500,
    "Sunday": 1700,
}

highest_day = None
lowest_day = None
highest_sales = None
lowest_sales = None
days_2000_or_more = 0

for day, amount in sales.items():
    if highest_sales is None or amount > highest_sales:
        highest_sales = amount
        highest_day = day

    if lowest_sales is None or amount < lowest_sales:
        lowest_sales = amount
        lowest_day = day

    if amount >= 2000:
        days_2000_or_more += 1

difference = highest_sales - lowest_sales

print("WEEKLY SALES REPORT")
print("-------------------")
print(f"Highest Sales Day: {highest_day}")
print(f"Highest Sales: {highest_sales}")
print(f"Lowest Sales Day: {lowest_day}")
print(f"Lowest Sales: {lowest_sales}")
print(f"Sales Difference: {difference}")
print(f"Days with sales >= 2000: {days_2000_or_more}")
