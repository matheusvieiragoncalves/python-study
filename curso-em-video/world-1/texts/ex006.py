# Exercise 006: Texts
# Create a program that reads a person name and shows the first name and last name separately.
# Example: "John Doe" -> First name: "John", Last name: "Doe"

name = str(input('Enter a name: '))

print(f'Name provided: {name}')
print(f'First Name: {name.split()[0].strip()}')
print(f'Last Name: {name.split()[len(name.split()) - 1].strip()}')
print(f'Name separately: {'-'.join(name.split())}')
