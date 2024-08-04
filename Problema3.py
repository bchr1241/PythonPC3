import math

class CIRCULO:
    def __init__(self, radio):
        try:
            self.radio = float(radio)
        except ValueError:
            raise ValueError("El radio debe ser un número válido")

    def calculoarea(self):
        return math.pi * self.radio **2

def main():
    while True:
        try:
            x = input("Ingrese el radio de un círculo para hallar su área: ")
            y = input("Ingrese el radio de otro redondo para hallar su área: ")

            CIRCULO1 = CIRCULO(x)
            CIRCULO2 = CIRCULO(y)

            Area_Circulo1 = CIRCULO1.calculoarea()
            Area_Circulo2 = CIRCULO2.calculoarea()

            print(f"El área del círculo 1 es {Area_Circulo1} y el área del círculo 2 es {Area_Circulo2}")
            
            break

        except ValueError:
            print("Ingrese valores correctos")
        except Exception:
            print("Error inesperado. Favor de ingresar nuevamente los valores.")

if __name__ == "__main__":
    main()