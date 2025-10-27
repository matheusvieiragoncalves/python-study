# Exercise 009: Arithmetic Operators
# Create an algorithm that takes a value and adds a 15% increase

originalPrice = float(input('Enter with a price: '))
increase = 15

finalPrice = originalPrice + (originalPrice * increase / 100)

print(f'Final price with 15% increase is {finalPrice}')
