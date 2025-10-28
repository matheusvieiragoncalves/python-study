


time = int(input('Amount years have your car? '))

if time <= 3:
    print('Your car is new!')
else:
    print('Your car is old!')

print('Your car is new!' if time <= 3 else 'Your car is old!') # is comparable to ternary conditional operator in orther languages


note1 = float(input('Enter your first grade: '))
note2 = float(input('Enter your second grade: '))
average = (note1 + note2) / 2

if average >= 6:
    print(f'Your average is {average:.1f}. You are approved!')
else:
    print(f'Your average is {average:.1f}. You are disapproved!')

print(f'Your average is {average:.1f}. You are {"approved" if average >= 6 else "disapproved"}!')