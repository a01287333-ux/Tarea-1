import math
def main():
    #Desarrolla un programa en Python que determine el largo que debe tener una escalera, la cual se necesita para alcanzar una altura determinada, cuando se pone contra una casa.
    import math
#Entradas

#Un número que corresponde a la altura de la casa (flotante positivo) y el ángulo en grados (entero positivo), en ese orden.
    altura = float(input("Altura de la casa: "))
    angulo = float(input("Angulo en grados: "))

    angulo_radianes = math.radians(angulo)
    largo = altura / math.sin(angulo_radianes)

    largo_redondeado = round(largo)

#Salida

#Un número, un número que representa el largo que debe tener la escalera. IMPORTANTE: Redondea el número para que el resultado sea entero. Utiliza la función adecuada que te provee Python para realizar un redondeo.
    print("Litros a comprar:", largo_redondeado)

if __name__ == '__main__':
    main()
