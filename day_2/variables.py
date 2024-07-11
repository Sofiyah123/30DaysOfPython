import math

#Day 2: 30 Days of python programming
first_name = "sofiat"
last_name = 'ibrahim'
full_name = 'ibrahim sofiat'
country ='Nigeria'
city ='ilorin'
age =27
year = 1997
is_married =True
is_true ='yes'
is_light_on ='yes'
middle_name, other_name,employment_status ='titilayo', 'morenike', 'not yet employed'

#Exercise 2:level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country ))
print(type(city))
print(type(age))
print(type(year ))
print(type(is_married))
print(type(is_true ))
print(type(is_light_on ))
# print(type(middle_name, other_name,employment_status ))
print(len(first_name))
if(len(first_name) > len(last_name)):
    print('firstname is longer than last name')
else:
    print('lastname is longer than firstname')

num_one = 5
num_two = 4
total = int(num_one) + int(num_two)
print(total)
product = num_one * num_two
print(product)
division = num_one/num_two
print(division)
remainder = (num_one % num_two)
print(remainder)
variable_expo = (num_one**num_two)
print(variable_expo)
floor_division = math.floor(num_one)/math.floor(num_two)
print(floor_division)
pie = 3.145
area_of_circle = pie * 30 *30
print(area_of_circle)
circumference_of_circle = 2 * pie * 30
print(circumference_of_circle)
radius = (int(input('Enter value for radius ')))
area = pie * radius * radius
first_name = input('Enter value for first name ')
last_name = input('Enter value for last name ')
country = input('Enter value for Country ')
age = int(input('Enter value for age '))
# help(str)
print('multiplying complex numbers: ', (1 + 1j) * (1 - 1j))