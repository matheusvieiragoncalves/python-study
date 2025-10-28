# Exercise 005: Texts
# Create a program that reads any phrase and shows:
# - How many times the letter "A" appears.
# - In which position it appears the first time.
# - In which position it appears the last time.

phrase = str(input('Enter a phrase: '))

for i in range(len(phrase)):
  print(f'[{phrase[i].upper():^4}]', end="")

print("")

for i in range(len(phrase)):
  print(f'[{i:^4}]', end="")

print("")

print(f'The phrase has {phrase.lower().count('a')} letters "A"')
print(f'The letters "A" find first in position {phrase.lower().find('a')}')
print(f'The letters "A" find last in position {phrase.lower().rfind('a')}')
