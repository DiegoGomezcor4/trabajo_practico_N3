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

def ingresar_numeros():
    numeros = []

    while True:
        entrada = input('Ingrese un numero entero o "fin" para ternminar: ')

        if not entrada:  # Si la entrada esta vacia
            if not numeros:  # Y la lista de números también está vacía
                print("Tiene que ingresar por lo menos un numero.")
                continue

        if entrada.lower() == 'fin' and numeros: # si ingresa fin, inicia las operaciones sobre la lista
            print('fin de la carga')
            break
        else:
            print('Tiene que ingesar por lo menos un numero')
        
        if entrada.isdigit() or entrada[0] == '-' and entrada[1:].isdigit(): # si es nunero entero positivo o negativo
            numero = int(entrada)
            numeros.append(numero)

        else:
            print('la entrada no es valida por favor ingrese un numero entero. ')

        print(numeros)
  
    return numeros  


def maximo_en_lista(lis):
    maximo = max(lis)
    print("El maximo de la lista es: ", maximo)



def segundo_maximo(lis):
    #convierte en conjunto para eliminar elementos duplicados, y los ordena de manera descendente
    numeros_ordenados = sorted(set(lis), reverse=True)

    #si la longitud de la lista es mayor que uno toma el segundo elemento sino, asigna none a la variable segundo maximo
    segundo_maximo = numeros_ordenados[1] if len(numeros_ordenados) > 1 else None
    print("El segundo maximo es: ", segundo_maximo)



def minimo_en_lista(lis):
    minimo = min(lis)
    print("El mínimo es:", minimo)



def multiplicar_elementos(lis):
    multiplicacion = 1
    for elemento in lis:
        multiplicacion *= elemento
    print("La multiplicación de todos los números es:", multiplicacion)


def contar_pares_impares(lis):
    pares = 0
    for elemento in lis:
        if elemento % 2 == 0:
            pares += 1

    impares = len(lis) - pares

    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)


def remover_repetidos(lis):
    elementos_sin_repetir = list(set(lis))
    print("Lista sin elementos repetidos:", elementos_sin_repetir)




# Ingresan los numeros
lista = ingresar_numeros()

# a. Determinar el maximo
maximo_en_lista(lista)

# b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
segundo_maximo(lista)

#c. Determinar el mínimo.
minimo_en_lista(lista)

#d. Calcular la multiplicación de  todos los números de la lista.
multiplicar_elementos(lista)

#e. Contar los valores pares e impares.
contar_pares_impares(lista)

#f. Remover los elementos repetidos
remover_repetidos(lista)






