"""
5. Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el
usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos.  Cada uno
de los números ingresados por el usuario deberá ser almacenado en una lista. A
continuación, realice las siguientes tareas:
a. Determinar el máximo.
b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
c. Determinar el mínimo.
d. Calcular la multiplicación de  todos los números de la lista.
e. Contar los valores pares e impares.
f. Remover los elementos repetidos
"""


numeros = []


while True:
    entrada = input('Ingrese un numero entero o "fin" para ternminar: ')
    if entrada.lower == 'fin':
        break
    if entrada.isdigit() or entrada[0] == '-' and entrada[1:].isdigit(): # si es nunero entero positivo o negativo
        numero = int(entrada)
        numeros.append(numero)
    else:
        print('la entrada no es valida por favor ingrese un nujmero entero. ')
        