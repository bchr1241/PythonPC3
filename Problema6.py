class PRODUCTO:
    def __init__(self, nombre, año, tipo, precio):
        try:
            self.nombre = nombre
            self.año = año
            self.tipo = tipo
            self.precio = precio
        except Exception:
            raise Exception("Ingrese los datos correctamente")

    def __str__(self):
        return f"Nombre: {self.nombre}, Año: {self.año}, Tipo: {self.tipo}, Precio: ${self.precio:.2f}"
            
class CATALOGO:
    def __init__(self):
        self.productos = []

    def agregarproducto(self, producto):
        if isinstance(producto, PRODUCTO):
            self.productos.append(producto)
        else:
            raise ValueError("El objeto debe ser una instancia de la clase Producto")
        
    def mostrarproductos(self):
        if not self.productos:
            print("El catálogo está vacío")
        for producto in self.productos:
            print(producto)

    def filtroaño(self, año):
        filtrado = [producto for producto in self.productos if producto.año == año]
        if not filtrado:
            print(f"No se encontraron productos del año {año}")
        else:
            for producto in filtrado:
                print(producto)

    def filtrotipo(self, tipo):
        filtrado = [producto for producto in self.productos if producto.tipo == tipo]
        if not filtrado:
            print(f"No se encontraron productos del tipo {tipo}")
        else:
            for producto in filtrado:
                print(producto)

def main():
    catalogo = CATALOGO()

    producto1 = PRODUCTO("Motor V200", 2010, "Hidráulica", 1000)
    producto2 = PRODUCTO("Batería", 2024, "Electrónica", 150)
    producto3 = PRODUCTO("Pastillas de Freno", 2015, "Seguridad", 100)

    catalogo.agregarproducto(producto1)
    catalogo.agregarproducto(producto2)
    catalogo.agregarproducto(producto3)

    print("Los productos en el catálogo son los siguientes: ")
    catalogo.mostrarproductos()
    print()

    print("Productos del año 2024: ")
    catalogo.filtroaño(2024)
    print()

    print("Productos de tipo 'Seguridad' :")
    catalogo.filtrotipo("Seguridad")

if __name__ == "__main__":
    main()


        