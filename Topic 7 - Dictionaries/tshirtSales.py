days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sales = []
total_sales = 0

up_arrow = chr(8593)   # ↑
down_arrow = chr(8595)    # ↓

for day in days:
  sales.append(int(input(f"Enter the number of t-shirts sold on {day}: ")))
  total_sales += sales[-1]  # Add the sale immediately to the total

average_sales = total_sales / len(days)

print(f"Total sales: {total_sales}, average per day: {average_sales:.2f}")

print("-" * 40)  # Print a separator for the table
print(f"{'Day':<15}{'Sales':>10}{'Trend':>10}")  # Print table headers
print("-" * 40)  # Print a separator for the table

for i, day in enumerate(days):
  arrow = down_arrow if sales[i] < average_sales else up_arrow
  print(f"{day:<15}{sales[i]:>10}{arrow:>10}")
