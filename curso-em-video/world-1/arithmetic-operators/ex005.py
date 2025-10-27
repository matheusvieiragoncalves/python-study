# Exercise 005: Arithmetic Operators
# Create a program to read a interger number and show your multiplication table

number = int(input('Enter with a interger number: '))

i = 0

while (i <= 10):
    print(f'{number} X {i} = {number * i}')
    i += 1

for i in range(11):
    print(f'{number} X {i} = {number * i}')