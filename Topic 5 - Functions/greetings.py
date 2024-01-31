def greeting(name):
  """Returns a very excited greeting to the user."""
  return "HELLO " + name.upper() + "!!!!"

# Get the user's name
user_name = input("What is your name? ")

# Call the greeting function and print the excited greeting
excited_greeting = greeting(user_name)
print(excited_greeting)
