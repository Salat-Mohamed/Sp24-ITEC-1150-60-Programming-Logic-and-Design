import random

def print_numbered_guest_list(guests):
   """Prints a numbered list of guests."""
   for i, guest in enumerate(guests, start=1):
       print(f"{i}. {guest}")

# Part 1: Create an empty list
guests = []

# Part 2: Add guests to the list
while True:
   name = input("Enter a guest name (or press Enter to stop): ")
   if not name:
       break
   if name in guests:
       print("That name is already on the list.")
   else:
       guests.append(name)

# Part 3: Print the initial guest list
print("\nInitial guest list:")
print_numbered_guest_list(guests)

# Part 4: Delete guests
while guests:
   choice = input("\nWould you like to delete a guest (y/n)? ")
   if choice.lower() != 'y':
       break

   name_or_index = input("Enter the name or index of the guest to delete: ")

   try:
       index = int(name_or_index) - 1  # Adjust for 1-based indexing
       if 0 <= index < len(guests):
           guests.pop(index)
           print(f"{guests[index]} has been removed from the list.")
       else:
           print("Invalid index.")
   except ValueError:
       if name_or_index in guests:
           guests.remove(name_or_index)
           print(f"{name_or_index} has been removed from the list.")
       else:
           print("Name not found on the list.")

# Part 5: Print the updated guest list (using function)
print("\nUpdated guest list:")
print_numbered_guest_list(guests)

# Part 6: Select prize winners
while True:
   num_prizes = input("\nHow many prizes would you like to give out? ")
   try:
       num_prizes = int(num_prizes)
       if 0 <= num_prizes <= len(guests):
           break
       else:
           print("Invalid number of prizes. Please enter a number between 0 and the total number of guests.")
   except ValueError:
       print("Invalid input. Please enter a number.")

# Ensure unique winners
winners = random.sample(guests, num_prizes)

# Part 7: Print final information
print("\nFinal guest list information:")
print(f"Total number of guests: {len(guests)}")
print_numbered_guest_list(guests)
print(f"\nPrize winners: {', '.join(winners)}")
