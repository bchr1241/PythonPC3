def main():
    while True:
        try:
            fraccion = input("Ingrese una fraccion (X/Y): ")
            x, y = map(int, fraccion.split('/'))

            if y==0:
                raise ZeroDivisionError("No se puede dividir por cero (0)")

            if x>y:
                raise ValueError("El numerador no puede ser mayor al denominador")
            
            porcentaje = (x/y)*100

            if porcentaje < 1:
                print ("E")
            elif porcentaje >99:
                print ("F")
            else:
                print(f"{round(porcentaje)}%")

            break

        except ZeroDivisionError:
            print("Por favor introduce una fracción donde el denominador sea distinto a 0 : Y<>0")
        except ValueError:
            print("Por favor introduce una fracción donde el numerador sea menor o igual al denominados y ambos sean números enteros: X<=Y")
        

        
if __name__ == "__main__":
    main()

