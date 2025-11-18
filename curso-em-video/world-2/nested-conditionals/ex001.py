# Exercise 001: Nested Conditionals
""" Type a program to aprove bank loan for house purchase. The program should ask the value of the house, 
the salary of the buyer and in how manu years he/she will pay."""
# Calcule the value of the monthly installment, which cannot exceed 30% of the salary, otherwise the loan will be denied.

salary = float(input('Informe seu salário: '))
house_value = float(input('Informe o valor da casa: '))
years_amount = float(input('Quantos anos quer pagar: '))

FEES = 25
NUMBER_OF_MONTHS_IN_THE_YEAR = 12
MAX_SALARY_PERCENTAGE = 30

total_pay_with_fees = (house_value + house_value * FEES / 100)
monthly_installment = total_pay_with_fees / (years_amount * NUMBER_OF_MONTHS_IN_THE_YEAR)

print(f'Total to pay: {total_pay_with_fees:.2f}')
print(f'Monthly installment: {monthly_installment:.2f}')

print('-=' * 10)

salary_percetage_calculated = salary * MAX_SALARY_PERCENTAGE / 100

if(monthly_installment > salary_percetage_calculated):
    
    print(f'rejected')
    print('-=' * 10)

    print(f'The monthly installment (R$ {monthly_installment:.2f}) is greater than the {MAX_SALARY_PERCENTAGE}% of salary: R$ {salary_percetage_calculated:.2f}')
else:
    print(f'Approved')
