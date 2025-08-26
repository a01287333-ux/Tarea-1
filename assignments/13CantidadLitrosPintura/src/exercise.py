import math
def main():
    #escribe tu código abajo de esta línea
    import math
#Entradas

    area = float(input("Area a pintar en metros: "))

#El área a pintar (número flotante)

#La cantidad de metros cuadrados que se pueden cubrir con un litro de pintura (número flotante)
    cobertura = float(input("Rendimiento (m2/l): "))

    litros_necesarios = math.ceil(area / cobertura)
#Salida

#La cantidad de litros a pintar (número entero)
    print("Litros a comprar:", litros_necesarios )


if __name__ == '__main__':
    main()
