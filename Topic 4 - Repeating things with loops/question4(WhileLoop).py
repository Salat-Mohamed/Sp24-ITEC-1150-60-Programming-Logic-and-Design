# Print the title of the quiz
print("Quiz program!")

# Initialize variables for attempts and answer
attempts = 0
answer = ""

# Continue looping as long as attempts are within the limit and the answer is incorrect
while attempts < 3 and answer.lower() != "madison":
  # Get the user's answer
  answer = input("What is the capital of Wisconsin? ")

  # Increment the attempt counter
  attempts += 1

  # Check if the answer is correct
  if answer.lower() == "madison":
    print("Correct!")
  else:
    print("Sorry, that is not right. Please try again.")

# If the loop ended without a correct answer, provide the correct answer
if answer.lower() != "madison":
  print("Sorry, you ran out of guesses. The answer is \"Madison\".")
