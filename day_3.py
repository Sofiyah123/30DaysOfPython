# age = 27
# height= 35.3
# complex_variable = 1 + 1j
# base = float(input("Enter value for base "))
# height = float(input("Enter value for height "))
# area_of_triangle = 0.5 * base * height
# print(f'area of triangle = {area_of_triangle}')
# first_side_triangle = int(input('Enter value for first side of the triangle '))
# second_side_triangle = int(input('Enter value for second side of the triangle '))
# Third_side_triangle = int(input('Enter value for Third side of the triangle '))
# perimeter_of_triangle = first_side_triangle * second_side_triangle * Third_side_triangle
# length_of_rectangle = int(input("Enter value for length"))
# width_of_rectangle = int(input("Enter value for breadth"))
# area_of_rectangle = length_of_rectangle * width_of_rectangle
# perimeter_of_rectangle = 2 * length_of_rectangle * width_of_rectangle
# radius_of_circle = int(input("Enter value for Radius of circle"))
# pie =3.145
# area_of_circle = pie * radius_of_circle * radius_of_circle
# perimeter_of_circle = 2 * pie * radius_of_circle
# if (len('python') == len('dragon')):
#     print('the two word are of the same length')

# else:
#     print('they are not of the same length')

print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print( 'on' not in 'dragon' and 'on' not in 'python')
length_of_python = float(len('python'))
length_of_python_in_string = str(length_of_python)
print('length of python = ', length_of_python)
print(length_of_python_in_string)
for i in range(1,11):
    if i % 2 == 0:
        print(f'{i} is even number')
    continue
print(7 // 2 is int(2.7))
print(type('10') is type(10))
print(type(9.8) == type(10))
hours = int(input("Enter value for hours "))
rate_per_hours = int(input("Enter value for rate per hours "))
weekly_earning = hours * rate_per_hours
print(f'Your weekly earning is {weekly_earning}')

#program to print a table
for number in range (1,6):
    print(f'{number}\t{number**0}\t{number**1}\t{number**2}\t{number**3}\n')