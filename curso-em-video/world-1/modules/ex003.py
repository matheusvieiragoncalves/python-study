# Exercise 003: Modules
# Create a program to read an angle and show your sine, cosine and tangent

from math import cos, sin, tan, radians

angle = float(input('Type to angle: '))
angleRad = radians(angle)

print(f'This sine is {sin(angleRad):.0f}')
print(f'This cosine is {cos(angleRad):.0f}')
print(f'This tangent is {tan(angleRad):.0f}')
