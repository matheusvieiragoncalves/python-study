# Exercise 005: Modules
# create a program to randomly sort the order of a list

from random import randint, shuffle

names = ['Matheus', 'Giovanna', 'João', 'Maria']

# count = 1

# while names.__len__() > 0:
#   drawIndex = randint(0, names.__len__() - 1)
#   drawName = names[drawIndex]

#   print(f'{count} - {drawName}')
#   names.remove(drawName)
#   count += 1

shuffle(names) # Embaralha

print(names)