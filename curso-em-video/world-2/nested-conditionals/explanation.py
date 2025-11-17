name = str(input('Digite seu nome: '))

if name == 'Pedro':
    print('Que nome bonito você tem!')
elif name == 'Giovanna':
    print('Belo nome feminino!')
elif name in 'Jorge Marcos Thiago':
    print('Nome bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print(f'Seu nome é {name}.')

