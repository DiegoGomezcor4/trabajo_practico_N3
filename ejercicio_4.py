"""
4. Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”],
realizar lo siguiente:
a. Imprimir la cantidad de elementos que tiene la lista.
b. Imprimir el primer y último elemento.
c. Imprimir el resto.
d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de
la lista. Quitar el elemento correspondiente de esa posición.
f. Imprimir la lista en orden inverso.
g. Vaciar la lista.
"""

paises = ['Argentina' ,'Brasil', 'Bolivia' ,'Paraguay' ,'Venezuela']

# a.
print(f'a. Cantidad de elementos de la lista: {len(paises)}')
print()

# b.
print('b. ')
print(f'El primer elemento es: {paises[0]}')
print(f'El ultimo elemento es: {paises[-1]}')
print()

# c.
print('c.')
print('El resto de los elementos son: ')
for i in range(1, len(paises) - 1):
    print(paises[i])
print()

#d .
print('d. ')
pais_buscado = input('Ingrese un pais: ')

if pais_buscado in paises:
    print(f'el pais {pais_buscado}, se encuenta en la posicion {paises.index(pais_buscado)}')
else:
    print('el pais no se encuentra en la lista')

print()

#e .
print('e. ')
numero = int(input(f'Ingrese un numero igual o menor que {len(paises)}: '))
if numero <= len(paises):
    pais_eliminado = paises.pop(numero - 1)
    print(f'se ha eliminado el pais {pais_eliminado} de la lista')
else:
    print(f'el numero ingresado no es menor o igual a {len(paises)}')

for pais in paises:
    print(pais)
print()

#f .
print('f. Imprimiendo la lista en orden inverso: ')
for i in range(len(paises) - 1, -1, -1):
    print(paises[i])

print()

#g .
print('g. ')
paises.clear()
print('La lista a sido vaciada ', paises)
