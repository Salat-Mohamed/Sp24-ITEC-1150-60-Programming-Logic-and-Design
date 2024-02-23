# list of int values
lab_numbers = [1,2,3,4,5,6,7,8,9,10]

# list of float values
temps = [78,87.5,67.7,56.3,66.3,98.4,67.9]
first_day_temp = temps[0]
print(f'The first day of the week was {first_day_temp}F')
temps[3] = 66.3
print(temps)

# list of different things
example = [False, 4, 1234.567 , 'Hello']

# list of different things
example = [example, temps,lab_numbers, [1,2,3]]
