# Display information about an input variable

variable = input("Enter something: ")

print(f'The type of the input is {type(variable)}')
print(f'Is it alphabetic? {variable.isalpha()}')
print(f'Is it numeric? {variable.isnumeric()}')
print(f'Is it alphanumeric? {variable.isalnum()}')
print(f'Is it uppercase? {variable.isupper()}')
print(f'Is it lowercase? {variable.islower()}')
print(f'Is it decimal? {variable.isdecimal()}')
print(f'Is it space? {variable.isspace()}')
print(f'Is it printable? {variable.isprintable()}')