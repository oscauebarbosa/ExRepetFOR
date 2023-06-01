qtclientes = int (input ('Insira a quantidade de clientes: '))
soma = 0
for n in range (1,qtclientes + 1):
    temperatura = float (input('Digite a temperatura: '))
    soma += temperatura
    if temperatura< 37.2:
        print('Está normal')
    elif 37.3>=temperatura<38:
        print('Está em estado febril')
    elif temperatura>=38 and temperatura<=39:
        print('com Febre')
    elif temperatura>39:
        print('Febre alta')
media = soma/qtclientes
print('A média das temperaturas é: ', media, 'e a quantidade de clientes é: ', qtclientes)