# Exercise 003: Arithmetic Operators
# Create a program to read two grades from a student, calculate and display their average

note1 = float(input('Enter your first note: '))
note2 = float(input('Enter your second note: '))

avarage = (note1 + note2) / 2

print('This final avarage entires {} and {} is {}'.format(note1, note2, avarage))