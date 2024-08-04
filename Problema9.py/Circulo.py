import math

class CIRCULO:
    def __init__(self, radio):
        try:
            self.radio = float(radio)
            if self.radio <= 0:
                raise ValueError("El radio debe ser un número positivo")
        except ValueError:
            raise ValueError("El radio debe ser un número válido y positivo")

    def calculoarea(self):
        return math.pi * self.radio ** 2