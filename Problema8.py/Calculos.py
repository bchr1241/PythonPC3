import Operaciones

def main():
    while True:
        try:
            print("Operaciones disponibles:")
            print("1. Suma")
            print("2. Resta")
            print("3. Producto")
            print("4. División")
            print("5. Salir")

            opcion = input("Seleccione una operacion del 1 al 5: ")

            if opcion == '5':
                break

            a = input("Ingrese el primer número: ")
            b = input("Ingrese el segundo número: ")

            if opcion == '1':
                resultado = Operaciones.suma(a, b)
            elif opcion == '2':
                resultado = Operaciones.resta(a, b)
            elif opcion == '3':
                resultado = Operaciones.producto(a, b)
            elif opcion == '4':
                resultado = Operaciones.division(a, b)
            else:
                raise ValueError("Opción no válida. Seleccione una opción correcta")
                continue

            print(f"El resultado de la operación es: {resultado}")

        except Exception:
            raise Exception("Error inesperado. Ingrese los datos nuevamente")

if __name__ == "__main__":
    main()
