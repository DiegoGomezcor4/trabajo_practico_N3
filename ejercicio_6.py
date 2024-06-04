"""
6. Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
de una lista vacía:
a. Agregar un elemento al final.
b. Agregar un elemento al principio.
c. Quitar un elemento al final.
d. Quitar un elemento al principio.
"""




while True:
    print('¿Que accion desea realizar?')
    print('a. Agregar un elemento al final')
    print('b. Agregar un elemento al principio')
    print('c. Quitar un elemento al final')
    print('d. Quitar un elemento al principio')
    print('e. Mostrar la lista')
    print('q. Sallir')

    opcion = input('Ingrese una opcion: ')

    if opcion == 'a':
        elemento = input('Ingrese el elemento que desea agregar al final: ')
        lista_agregar_final(elemento)
    elif opcion == 'b':
        elemento = input('Ingrese el elemento que desea agregar al principio: ')
        lista_agregar_principio(elemento)
    elif opcion == 'c':
        lista_quitar_final()
    elif opcion == 'd':
        lista_quitar_principio()
    elif opcion == 'e':
        lista_mostrar()
    elif opcion == 'q': 
        print('saliendo')
        break
    else:
        print('Opcion no valida')