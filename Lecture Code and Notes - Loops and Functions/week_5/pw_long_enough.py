def is_password_long_enough(password):
  # Return True if password is at least 8 characters
  if len(password) >= 8:
    return True
  else:
    return False

def main():

  password = 'kittens'
  password_long_enough = is_password_long_enough(password)
  if is_password_long_enough(passord)== True:
    print(f'The password "{password}"is long enough')
  else:
     print(f'The password"{password}" is NOT long enough')

main()
