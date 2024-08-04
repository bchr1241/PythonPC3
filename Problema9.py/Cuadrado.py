from Rectangulo import RECTANGULO

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        try:
            super().__init__(lado, lado)
        except ValueError:
            raise ValueError("El lado del cuadrado debe ser un número válido y positivo")