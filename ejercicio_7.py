"""
7. Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al
usuario:
a. Agregar nuevas tareas pendientes.
b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
de la lista de pendientes a la de terminadas.
Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas
listas.
"""


def agregar_tarea_pendiente(tareas_pendientes):
    tarea = input('Ingrese una tarea para agregar a pendientes: ')
    tareas_pendientes.append(tarea)
    mostrar_listas()


def marcar_tarea_como_terminada(tareas_pendientes, tareas_terminadas):
    tarea = input('Ingrese la tarea a marcar como terminada: ')
    if tarea in tareas_pendientes:
        tareas_pendientes.remove(tarea)
        tareas_terminadas.append(tarea)
    else:
        print('la tarea no se encuentra como pendiente!!!')
    mostrar_listas()
    


def mostrar_listas():
    print('Tareas pendientes ', lista_pendientes)
    print('Tareas terminadas', lista_terminadas)


lista_pendientes = []
lista_terminadas = []

while True:
    print('Elija una opcion:')
    print('a. Agregar una nueva tarea pendiente')
    print('b. Marcar una tarea pendiente como terminada')
    print('c. Mostrar las listas de tareas')
    print('q. Salir')

    opcion = input().lower();

    match opcion:
        case 'a':
            agregar_tarea_pendiente(lista_pendientes)
        case 'b':
            marcar_tarea_como_terminada(lista_pendientes, lista_terminadas)
        case 'c':
            mostrar_listas()
        case 'q':
            print('saliendo del programa')
            break
        case _:
            # Código a ejecutar si ninguno de los casos es igual a variable
            pass

    

