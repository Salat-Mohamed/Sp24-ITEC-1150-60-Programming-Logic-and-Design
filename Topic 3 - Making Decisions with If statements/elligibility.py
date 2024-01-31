def check_senator_eligibility(desired_state, age, citizen_years, current_state):
  """
  Checks if a user is eligible to be a senator in a state based on age, citizenship, and residency.

  Args:
    desired_state: The state the user wants to represent (string).
    age: The user's age (int).
    citizen_years: The number of years the user has been a US citizen (int).
    current_state: The state the user currently lives in (string).

  Returns:
    None. Prints a message based on the user's eligibility.
  """
  eligible = True  # Assume eligibility initially
  reasons = []  # List to store reasons for ineligibility (optional)

  if age < 30:
    eligible = False
    reasons.append("not old enough (must be at least 30)")
  if citizen_years < 9:
    eligible = False
    reasons.append("not a US citizen for long enough (must be at least 9 years)")
  if desired_state != current_state:
    eligible = False
    reasons.append("does not live in the desired state")

  if eligible:
    print("Congratulations! You are eligible to be a senator in", desired_state)
  else:
    message = "Sorry, you are not eligible to be a senator in " + desired_state
    if reasons:
      message += " because you are " + ", ".join(reasons) + "."
    print(message)

# Get user input
desired_state = input("What state do you want to represent? ").upper()
age = int(input("How old are you? "))
citizen_years = int(input("How many years have you been a US citizen? "))
current_state = input("What state do you currently live in? ").upper()

# Check eligibility
check_senator_eligibility(desired_state, age, citizen_years, current_state)
