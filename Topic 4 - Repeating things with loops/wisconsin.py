print("Quiz program!")

correct_answer = "Madison"
attempts = 0

while attempts < 3:
  user_answer = input("What is the capital of Wisconsin? ")
  attempts += 1

  if user_answer.lower() == correct_answer:
    print("Correct!")
    break
  else:
    if attempts == 3:
      print("Sorry, you've used all your attempts. The correct answer is", correct_answer)
    else:
      print("Incorrect. You have", 3 - attempts, "attempts remaining.")

