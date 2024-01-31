# Print the title of the quiz
print("Quiz program!")

# Loop for 3 attempts
for attempt in range(3):
 # Get the user's answer
 answer = input("What is the capital of Wisconsin? ")

 # Check if the answer is correct (case-insensitive)
 if answer.lower() == "madison":
   print("Correct!")  # Provide positive feedback for a correct answer
   break  # Exit the loop if the answer is correct

 else:
   print("Sorry, that is not right. Please try again.")  # Provide feedback for incorrect answers

# If the loop ended without a correct answer, provide the correct answer
if answer.lower() != "madison":
 print("Sorry, you ran out of guesses. The answer is \"Madison\".")
