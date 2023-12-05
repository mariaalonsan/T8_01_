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

# Creación de algunos alumnos
alumno1 = Alumno("Ana", 3)
alumno2 = Alumno("Olivia", 10)
alumno3 = Alumno("Jaime", 7)

# Prueba del método calificacion
alumno1.calificacion()
alumno2.calificacion()
alumno3.calificacion()