star_id = input('Enter your StarID: ')

while len(star_id) != 8:
  print('Error - a valid starid has 8 characters')
  star_id = input('Enter your StarID: ')

print('Thank you, your starID is ' + star_id)
  
