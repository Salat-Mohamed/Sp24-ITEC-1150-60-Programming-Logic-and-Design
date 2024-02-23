def first_year_second_year(class_code):
  # if class_code is between 1000 and 1999, return 'First year'
  if class_code >= 1000 and class_code <= 1999:
    return 'First Year'
  elif class_code >= 2000 and class_code <= 2999:
    return 'Second Year'
  else:
    return 'Invalid Code'
    
def main():
  code =int(input('Please enter class code: '))
  result = first_year_second_year(code)
  print(result)

main()
