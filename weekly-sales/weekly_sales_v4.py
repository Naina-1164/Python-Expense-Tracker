"""Beginner Python: weekly sales target achievement."""

weekly_sales = {
    "Monday": 1200, "Tuesday": 1500, "Wednesday": 1100,
    "Thursday": 1800, "Friday": 2100, "Saturday": 2500,
    "Sunday": 1700,
}

def sales_target_summary(sales, target):
    target_met = 0
    for day, amount in sales.items():
        if amount >= target:
            target_met += 1
            print(f"{day} - Target Met")
        else:
            print(f"{day} - Below Target")

    total_days = len(sales)
    achievement_percentage = (target_met / total_days * 100) if total_days else 0
    print("Target Met Days:", target_met)
    print(f"Achievement Rate: {achievement_percentage:.2f}%")
    return target_met, achievement_percentage

if __name__ == "__main__":
    sales_target_summary(weekly_sales, 2000)
    print("\nBonus: Target ₹1500")
    sales_target_summary(weekly_sales, 1500)
