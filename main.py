from views import (
    crear_estudiante, obtener_todos, obtener_por_id,
    buscar_estudiantes, actualizar_estudiante, eliminar_estudiante,
)


def mostrar_lista(lista):
    if len(lista) == 0:
        print("No hay estudiantes.")
    for e in lista:
        print(e)


def opcion_crear():
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    carnet = input("Carnet: ").strip().upper()
    exito, mensaje = crear_estudiante(nombre, apellido, carnet)
    print(mensaje)


def opcion_ver_todos():
    mostrar_lista(obtener_todos())


def opcion_buscar():
    texto = input("Buscar (nombre, apellido o carnet): ").strip()
    mostrar_lista(buscar_estudiantes(texto))


def opcion_actualizar():
    try:
        id_estudiante = int(input("Id del estudiante: "))
    except ValueError:
        print("El id debe ser un número")
        return

    estudiante = obtener_por_id(id_estudiante)
    if estudiante is None:
        print("No existe ese id")
        return

    print("Deje vacío lo que no quiera cambiar.")
    nombre = input("Nombre [" + estudiante.nombre + "]: ").strip()
    apellido = input("Apellido [" + estudiante.apellido + "]: ").strip()
    carnet = input("Carnet [" + estudiante.carnet + "]: ").strip().upper()

    if nombre == "":
        nombre = estudiante.nombre
    if apellido == "":
        apellido = estudiante.apellido
    if carnet == "":
        carnet = estudiante.carnet

    exito, mensaje = actualizar_estudiante(id_estudiante, nombre, apellido, carnet)
    print(mensaje)


def opcion_eliminar():
    try:
        id_estudiante = int(input("Id del estudiante: "))
    except ValueError:
        print("El id debe ser un número")
        return
    exito, mensaje = eliminar_estudiante(id_estudiante)
    print(mensaje)


def main():
    while True:
        print()
        print("===== SISTEMA DE ESTUDIANTES =====")
        print("1. Crear estudiante")
        print("2. Ver todos")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("0. Salir")
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            opcion_crear()
        elif opcion == "2":
            opcion_ver_todos()
        elif opcion == "3":
            opcion_buscar()
        elif opcion == "4":
            opcion_actualizar()
        elif opcion == "5":
            opcion_eliminar()
        elif opcion == "0":
            print("Hasta luego")
            break
        else:
            print("Opción no válida")


main()