"""
2. Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
Imprimir por pantalla el resultado.
"""

numeros = []

for i in range(1,6):
    numero_ingresado = float(input(f'Ingrese un número en la posicion {i}: '))
    numeros.append(numero_ingresado)


numeros.sort()


print('Lista de numeros ordenada: ')
for numero in numeros:
    print(numero)