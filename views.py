from models import Estudiante
from shared.json_manager import GestorJSON

gestor = GestorJSON("data/estudiantes.json")


# ---------- CREAR ----------
def crear_estudiante(nombre, apellido, carnet):
    if nombre == "" or apellido == "" or carnet == "":
        return False, "Todos los campos son obligatorios"

    registros = gestor.leer()

    carnets = set()
    for r in registros:
        carnets.add(r["carnet"])
    if carnet in carnets:
        return False, "Ese carnet ya existe"

    if len(registros) == 0:
        nuevo_id = 1
    else:
        nuevo_id = registros[-1]["id"] + 1

    estudiante = Estudiante(nuevo_id, nombre, apellido, carnet)
    registros.append(estudiante.a_diccionario())
    gestor.guardar(registros)
    return True, "Estudiante creado con id " + str(nuevo_id)


# ---------- LEER ----------
def obtener_todos():
    lista = []
    for r in gestor.leer():
        lista.append(Estudiante.desde_diccionario(r))
    return lista


def obtener_por_id(id_estudiante):
    for e in obtener_todos():
        if e.id == id_estudiante:
            return e
    return None


# ---------- BUSCAR ----------
def buscar_estudiantes(texto):
    texto = texto.lower()
    encontrados = []
    for e in obtener_todos():
        if texto in e.nombre.lower() or texto in e.apellido.lower() or texto in e.carnet.lower():
            encontrados.append(e)
    return encontrados


# ---------- ACTUALIZAR ----------
def actualizar_estudiante(id_estudiante, nombre, apellido, carnet):
    registros = gestor.leer()

    for r in registros:
        if r["carnet"] == carnet and r["id"] != id_estudiante:
            return False, "Ese carnet ya lo tiene otro estudiante"

    for r in registros:
        if r["id"] == id_estudiante:
            r["nombre"] = nombre
            r["apellido"] = apellido
            r["carnet"] = carnet
            gestor.guardar(registros)
            return True, "Estudiante actualizado"

    return False, "No existe un estudiante con ese id"


# ---------- ELIMINAR ----------
def eliminar_estudiante(id_estudiante):
    registros = gestor.leer()
    nueva_lista = []
    for r in registros:
        if r["id"] != id_estudiante:
            nueva_lista.append(r)

    if len(nueva_lista) == len(registros):
        return False, "No existe un estudiante con ese id"

    gestor.guardar(nueva_lista)
    return True, "Estudiante eliminado"