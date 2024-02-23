todo_list = []

while True:
  task = input('Enter your task, or press enter to stop: ')
  if task: # any string that is not empty, is True
    todo_list.append(task)
  else:
    break
  
print('Thank you, your tasks are: ')
print(todo_list)
for task in todo_list:
  print(task)
  
