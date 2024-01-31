# Ask the user for the number of cents they have
cents = int(input("How many cents do you have? "))

# Check for different amounts of cents
if cents < 100:
   print("You have less than a dollar.")
elif cents == 100:
   print("You have exactly one dollar.")
else:
   print("You have more than one dollar.")

# Bonus question: Check for exact dollar amounts
if cents % 100 == 0:
   dollars = cents // 100
   print("You have an exact number of dollars: ", dollars)
