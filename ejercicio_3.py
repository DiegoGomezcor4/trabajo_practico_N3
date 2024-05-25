"""
3. Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
debajo la misma lista pero sólo con las frutas que añadió el usuario
"""

frutas = ['banana', 'manzana', 'pera']
nuevas_frutas = []

for i in range(1,4):
    nueva_fruta = input('Ingrese una fruta: ')
    nuevas_frutas.append(nueva_fruta)


frutas.extend(nuevas_frutas)

print()
print('Lista completa: ')
for fruta in frutas:
    print(fruta)


print()
print('frutas que añadio el usuario: ')
for fruta in nuevas_frutas:
    print(fruta)
