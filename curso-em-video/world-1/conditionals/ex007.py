# Exercise 007: conditionals
# Create a program that ask to funcionary's salary and calcule the increase according to the following criteria:
# - Salary up to R$ 1.250,00: increase of 15%
# - Salary above R$ 1.250,00: increase of 10%

salary = float(input('Enter a salary: R$'))

ROOM_FOR_FURTHER_INCREASE = 1250

if salary > ROOM_FOR_FURTHER_INCREASE:
    increase = 10
else:
    increase = 15

result = (salary * increase) / 100 + salary

print(f'This final salary is: R${result:.2f}')
