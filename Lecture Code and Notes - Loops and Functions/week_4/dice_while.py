import random

want_to_quit = ''

while not want_to_quit: # empty string is false, 'q' or any other string is true
  dice_value = random.randomint(1,6)
  print(f'You rolled a {dice_value}')
  want_to_quit = input('Roll again? Press enter to roll again, any other key to quit.')
