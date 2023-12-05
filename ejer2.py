class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f"Alumno {self.nombre} creado con éxito.")

    def calificacion(self):
        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}.")
        else:
            print(f"{self.nombre} ha suspendido con una nota de {self.nota}.")

    def __str__(self):
        return f"Alumno: {self.nombre}, Nota: {self.nota}"

# Creación de algunos alumnos
alumno1 = Alumno("Celia", 2)
alumno2 = Alumno("Alberto", 6)

# Realizando print de los objetos para visualizar la información del método __str__
print(alumno1)
print(alumno2)