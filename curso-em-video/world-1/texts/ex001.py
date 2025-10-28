# Exercise 001: Texts
# Create a program that reads a person name and displays:
# 1 - The name with all uppercase letters
# 2 - The name with all lowercase letters
# 3 - How many letters (without spaces) the name has
# 4 - How many letters the first name has

name = str(input('Enter your name: '))

print(name.upper())
print(name.lower())
print(len(name.replace(" ", "")))
print(len(name.split()[0]))