print('Hello, World!')

authorName = 'Matheus'
authorAge = 25
authorWeight = 79.5

print(authorName, authorAge, authorWeight)
print(f'{authorName} is {authorAge} years old and weighs {authorWeight} kg.')
print('{} is {} years old and weighs {} kg.'.format(authorName, authorAge, authorWeight))

# readerName = input('What is your name? ')
# readerAge = input('What is your age? ')
# readerWeight = input('What is your weight? ')

# print(readerName, readerAge, readerWeight)
# print(f'{readerName} is {readerAge} years old and weighs {readerWeight} kg.')
# print('{} is {} years old and weighs {} kg.'.format(readerName, readerAge, readerWeight))

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
sum = num1 + num2
print(f'The sum of {num1} and {num2} is {sum}.')
