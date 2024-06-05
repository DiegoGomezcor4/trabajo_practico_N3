"""
6. Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
de una lista vacía:
a. Agregar un elemento al final.
b. Agregar un elemento al principio.
c. Quitar un elemento al final.
d. Quitar un elemento al principio.
"""



# a, agregar un elemento al final.
def lista_agregar_final(elem,lis):
    lis.append(elem)
    print('Elemento agregado al final de la lista')
    print(lis)


#b. agregar un elememento al principio
def lista_agregar_principio(elem,lis):
    lis.insert(0,elem)
    print('Elemento agregado al principio de la lista')
    print(lis)


#c. quitar un elemento al final
def lista_quitar_final(lis):
    if lis:
        elemento = lista.pop()
        print(f'El elemento {elemento} fue removido del final de la lista ')
        print(lis)
    else:
        print('La lista esta vacia')


#d. Quitar un elemento del principio
def lista_quitar_principio(lis):
    if lis:
        elemento = lis.pop(0)
        print(f'El elemento {elemento} fue removido del principio de la lista')
        print(lis)
    else:
        print('La lista esta vacia.')

def lista_mostrar(lis):
    print('Contenido de la lista', lis)

lista = []

while True:
    print('¿Que accion desea realizar?')
    print('a. Agregar un elemento al final')
    print('b. Agregar un elemento al principio')
    print('c. Quitar un elemento al final')
    print('d. Quitar un elemento al principio')
    print('e. Mostrar la lista')
    print('q. Salir')

    opcion = input('Ingrese una opcion: ')

    if opcion == 'a':
        elemento = input('Ingrese el elemento que desea agregar al final: ')
        lista_agregar_final(elemento,lista)
    elif opcion == 'b':
        elemento = input('Ingrese el elemento que desea agregar al principio: ')
        lista_agregar_principio(elemento,lista)
    elif opcion == 'c':
        lista_quitar_final(lista)
    elif opcion == 'd':
        lista_quitar_principio(lista)
    elif opcion == 'e':
        lista_mostrar(lista)
    elif opcion == 'q': 
        print('saliendo')
        break
    else:
        print('Opcion no valida')