# Exercise 005: Arithmetic Operators
# Create a program to read a interger number and show your multiplication table

number = int(input('Enter with a interger number: '))

i = 0

print('=' * 30)

while (i <= 10):
    print('{:^8} X {:^8} = {:^8}'.format(number, i, number * i))
    i += 1

print('=' * 30)

for i in range(11):
    print('{:^8} X {:^8} = {:^8}'.format(number, i, number * i))

print('=' * 30)