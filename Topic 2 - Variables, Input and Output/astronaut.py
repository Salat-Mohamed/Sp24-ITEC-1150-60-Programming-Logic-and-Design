# Convert input to integers
num_rides = int(input("How many times did you ride the bus last month? "))
cost_per_ride = float(input("What is the cost of one bus ride? "))

# Calculate total cost
total_cost = num_rides * cost_per_ride

# Convert variables to strings and format output
output_rides = str(num_rides)
output_cost_per_ride = "${:.2f}".format(cost_per_ride)  # Format to two decimal places
output_total_cost = "${:.2f}".format(total_cost)  # Format to two decimal places

# Print the results
print(f"You rode the bus {output_rides} times last month. One bus ride costs {output_cost_per_ride}. Your total cost was {output_total_cost}")
