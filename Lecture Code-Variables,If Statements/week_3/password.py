secret_password = 'kittens'

password = input('Enter the secret password: ')

if password == secret_password:
  print('welcome, authorized user!')
else:
  print('sorry wrong password')
