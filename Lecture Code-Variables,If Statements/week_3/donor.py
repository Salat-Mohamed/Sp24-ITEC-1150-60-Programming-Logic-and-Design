weight = float(input('please enter your weight in pounds: '))
age = int(input('please enter your age in years: '))

if weight >= 110 and age >= 16:
  print('Great! you are eligile to be a blood donor.')
else:
  print('Sorry, you are not eligible')
  if age < 16:
    print('You are not old enough')
  if weight < 110:
    print('You do not weigh enough')
