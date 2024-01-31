for day in range(1, 32):
  if day == 1 or day == 21 or day == 31:
    suffix = "st"
  elif day == 2 or day == 22:
    suffix = "nd"
  elif day == 3 or day == 23:
    suffix = "rd"
  else:
    suffix = "th"
  print("January", day, suffix)
