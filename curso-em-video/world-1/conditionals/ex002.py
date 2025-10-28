# Exercise 002: conditionals
# Create a program that reads the cars velocity and checks if it exceeds 80 km/h
# Show a message indicating whether the driver was fined or not.
# fine is R$7.00 for each km above the limit.

carSpeed = float(input('Enter a velocity: '))

MAXIMUM_PERMITTED_SPEED = 80

if carSpeed > MAXIMUM_PERMITTED_SPEED:
    fine = (carSpeed - MAXIMUM_PERMITTED_SPEED) * 7
    print(f'fine of R${fine:.2f} applied')
else:
    print('speed not exceeded')
