# Create strings with multiple repeats
# For example, 'ha' repeaed 5 times is 'hahahahaha'

def main():
  string = input('Please enter a string: ')
  repeat = int(input('How many times to repeat? '))
  result = string_repeater(string, repeat)
  print(result)

def string_repeater(text,n:
  repeated_string = text * n
  return repeated_string
main()
