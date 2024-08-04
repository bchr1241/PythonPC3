class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = float(largo)
        self.ancho = float(ancho)

    def calculoareaR(self):
        return self.largo * self.ancho
    
class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

