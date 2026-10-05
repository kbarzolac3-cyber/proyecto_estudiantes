class Estudiante:
    def __init__(self, id_estudiante, nombre, apellido, carnet):
        self.id = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet

    def a_diccionario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "carnet": self.carnet,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["id"], datos["nombre"], datos["apellido"], datos["carnet"])

    def __str__(self):
        return f"[{self.id}] {self.nombre} {self.apellido} - Carnet: {self.carnet}"