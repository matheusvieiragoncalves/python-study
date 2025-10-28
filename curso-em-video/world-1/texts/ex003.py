# Exercise 003: Texts
# Create a program that reads a city name and tells if it starts with the name "Santo".

cityName = str(input('Enter a city name: '))

print(f'The city name start with a "Santo"? {cityName.split()[0].lower().strip() == 'santo'}')
