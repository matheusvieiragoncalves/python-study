# Exercise 007: Arithmetic Operators
# Create a program to read the height and width of a wall, calculate its area and the amount of paint to paint it
# 1L of paint to 2m2

wallHeight = float(input('Enter with a wall height: '));
wallWidth = float(input('Enter with a wall Width: '));

area = wallHeight * wallWidth

LITER_PER_AREA = 2;

print(f'wall height: {wallHeight}m')
print(f'wall Width: {wallWidth}m')
print(f'wall area: {area}m2')

print(f'Paint to fill all area: {area * LITER_PER_AREA}')
