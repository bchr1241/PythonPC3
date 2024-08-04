def suma(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        raise ValueError("Tipo de dato no válido")

def resta(a, b):
    try:
        return float(a) - float(b)
    except ValueError:
        raise ValueError("Tipo de dato no válido")

def producto(a, b):
    try:
        return float(a) * float(b)
    except ValueError:
        raise ValueError("Tipo de dato no válido")

def division(a, b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            raise ValueError("No es posible dividir entre cero")
        return a/b
    except ValueError:
        raise ValueError("Tipo de dato no válido")