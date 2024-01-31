def quiz(question, answer):
 """Asks a quiz question and verifies the user's answer."""

 print(question)
 user_answer = input("Your answer: ").lower()  # Convert user input to lowercase for comparison

 if user_answer == answer.lower():
   print("Correct!")
 else:
   print("Incorrect. The correct answer is", answer)

def main():
 """Calls the quiz function twice with different questions."""

 quiz("Which planet is closest to the sun?", "Mercury")
 quiz("Who painted the Mona Lisa?", "Leonardo da Vinci")

if __name__ == "__main__":
 main()
