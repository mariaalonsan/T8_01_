class Producto:
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print(f"Producto {self.nombre} creado con éxito.")

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: ${self.precio}, Tipo: {self.tipo}"

# Creación de algunos productos
producto1 = Producto("001", "Call of Duty", 69.99, "Videojuegos")
producto2 = Producto("002", "Queso", 2.35, "Alimentación")
producto3 = Producto("003", "Top Drapeado Negro", 22.95, "Ropa")
producto4 = Producto("004", "Goma de borrar", 69.99, "Papelería")

# Mostrar los datos de un producto
print(producto1)

# Modificar el precio de un producto
producto1.precio =59.99

# Mostrar los datos del producto después de modificar el precio
print(producto1)
