parking_time = float(input('How many hours have you parked? '))

# The max parking time allowed is 2 hours

if parking_time >= 2:
  print('Warining! You should move your car.')
  # can you print how many hours you are over?
  time_over = parking_time - 2
  print('You are ' + str(time_over) + ' hours overdue')
else:
  print('You are ok for parking, you still have time')
  # Can you print how many hours are left?
  time_left = 2 - parking_time
  print('You have ' + str(time_left) + ' hours left.')
print('This is the end of the program')
# pause the video
# write this code
# compare > version to the >= version
# which do you think is better?
