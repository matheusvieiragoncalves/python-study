# Exercise 006: Arithmetic Operators
# Create a program to enter a number in real and convert value to dollar. Search dollar current value in today using web API

import urllib.request
import json
import ssl

url = "https://api.exchangerate-api.com/v4/latest/USD"

context = ssl._create_unverified_context()
with urllib.request.urlopen(url, context=context) as response:
    data = json.loads(response.read())

# Valor do dólar em reais (BRL)
oneDollarInReal = data["rates"]["BRL"]

real = float(input('Enter with a value in real: '))

print(f'This origial value is R$ {real:.2f} and value converted is $ {real * oneDollarInReal:.2f}')

