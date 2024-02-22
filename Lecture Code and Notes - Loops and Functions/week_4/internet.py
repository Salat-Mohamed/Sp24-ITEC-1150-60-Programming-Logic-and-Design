from urllib import request       # used to connect to internet resources
from time import sleep           # sleep will pause the program for a time 

url = 'https://www.google.com'
seconds_to_sleep_between_checks = 3

while True:
  print('checking if online....')
  try:
    # Try to connect to the URL
    request.urlopen(url).read()
    print('You are probably online!')
    os.system('say hey, you are online!')
  except:
    # this code runs if can't connect to the URL
    print('You are not online')
    
  print(f'sleeping for{seconds_to_sleep_between_checks} seconds')
  print()
  sleep(seconds_to_sleep_between_checks)
