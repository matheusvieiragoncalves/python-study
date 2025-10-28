# Exercise 004: conditionals
# Create a program that ask the distance of a trip in km.
# Calculate the price of the ticket, charging R$0.50 per km for trips up to 200km
# and R$0.45 for longer trips.

distance = float(input('Enter a distance: '))

MAXIMUM_DISTANCE_WITH_OUT_DISCOUNT = 200

if distance <= MAXIMUM_DISTANCE_WITH_OUT_DISCOUNT:
    VALUE_PER_DISTANCE = 0.5
else:
    VALUE_PER_DISTANCE = 0.45

# also is possible use ternary, example:
# VALUE_PER_DISTANCE = 0.5 if distance <= MAXIMUM_DISTANCE_WITH_OUT_DISCOUNT else 0.45

print(f'Ticket value is R${distance * VALUE_PER_DISTANCE:.2f}')
