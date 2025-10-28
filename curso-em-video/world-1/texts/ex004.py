# Exercise 004: Texts
# Create a program that reads a person name and verify if name has "SILVA" in it.

name = str(input('Enter a name: ')).strip().lower()

print(f'Existis "Silva" in name? {name.find('silva') >= 0}')
print(f'Existis "Silva" in name? {'silva' in name}')
