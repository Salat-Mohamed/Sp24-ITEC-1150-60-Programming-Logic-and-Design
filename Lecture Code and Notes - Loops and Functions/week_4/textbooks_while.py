# while version textbook total program

total = 0
more_books = True

while more_books:
  book_price = float(input('Enter price of book$'))
  total = total + book_price
  any_more = input('Any more books? Enter "Y" for yes and "N" for no.')
  if any_more.upper() == 'N' # Can you accept 'n' to stop the loop
    more_books = False
print(f'The total of all the books is ${total}')
