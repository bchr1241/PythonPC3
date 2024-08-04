class RECTANGULO:
    def __init__(self, largo, ancho):
        try:
            self.largo = float(largo)
            self.ancho = float(ancho)
            if self.largo <= 0 or self.ancho <= 0:
                raise ValueError("El largo y el ancho deben ser números positivos")
        except ValueError:
            raise ValueError("El largo y el ancho deben ser números válidos y positivos")

    def calculoareaR(self):
        return self.largo * self.ancho