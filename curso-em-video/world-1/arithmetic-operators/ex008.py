# Exercise 008: Arithmetic Operators
# Create an algorithm that takes a value and adds a 5% discount

originalPrice = float(input('Enter with a price: '))
discount = 5

finalPrice = originalPrice - (originalPrice * discount / 100)

print(f'Final price with 5% discount is {finalPrice}')
