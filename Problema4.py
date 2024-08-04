class RECTANGULO:
    def __init__(self, largo, ancho):
        try:
            self.largo = float(largo)
            self.ancho = float(ancho)
        except ValueError:
            raise ValueError("El largo y/o ancho deben de ser números válidos")

    def calculoareaR(self):
        return self.largo * self.ancho
    
class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        try:
            super().__init__(lado, lado)
        except ValueError:
            raise ValueError("El lado del cuadrado debe de ser un número válido")

def main():
    while True:
        try:
            x = float(input("Ingrese el largo de un rectángulo: "))
            y = float(input("Ingrese el ancho del mismo rectángulo: "))

            RECTANGULO1 = RECTANGULO(x, y)

            z = float(input("Ingrese el lado de un cuadrado: "))

            CUADRADO1 = CUADRADO(z)

            area_rectangulo = RECTANGULO1.calculoareaR()
            area_cuadrado = CUADRADO1.calculoareaR()

            print(f"El área del rectángulo es {area_rectangulo} y el área del cuadrado es {area_cuadrado}")

            break

        except ValueError:
            print("Ingrese valores correctos")
        except Exception:
            print("Error inesperado. Favor de ingresar nuevamente los valores.")


if __name__ == "__main__":
    main()