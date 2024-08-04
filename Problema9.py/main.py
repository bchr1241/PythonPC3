from Circulo import CIRCULO
from Rectangulo import RECTANGULO
from Cuadrado import CUADRADO

def obtener_numero_positivo(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("El número debe ser positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    while True:
        print("\nMenú de Cálculo de Áreas:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            radio = obtener_numero_positivo("Ingrese el radio del círculo: ")
            circulo = CIRCULO(radio)
            area = circulo.calculoarea()
            print(f"El área del círculo es: {area}")

        elif opcion == '2':
            largo = obtener_numero_positivo("Ingrese el largo del rectángulo: ")
            ancho = obtener_numero_positivo("Ingrese el ancho del rectángulo: ")
            rectangulo = RECTANGULO(largo, ancho)
            area = rectangulo.calculoareaR()
            print(f"El área del rectángulo es: {area}")

        elif opcion == '3':
            lado = obtener_numero_positivo("Ingrese el lado del cuadrado: ")
            cuadrado = CUADRADO(lado)
            area = cuadrado.calculoareaR()
            print(f"El área del cuadrado es: {area}")

        elif opcion == '4':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")

if __name__ == "__main__":
    main()
