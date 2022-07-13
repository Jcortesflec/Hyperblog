class Conversion:

    def Colombia():
        pesos = input("¿cuantos pesos colombianos tienes? ")
        pesos = float(pesos)
        valor_dolar = 4608.65
        dolares = pesos / valor_dolar
        dolares = round(dolares , 2)
        dolares = str(dolares)
        print("tienes $"+dolares+" dolares")

    def Argentina():
        pesos = input("¿cuantos pesos argentinos tienes? ")
        pesos = float(pesos)
        valor_dolar = 127.59
        dolares = pesos / valor_dolar
        dolares = round(dolares , 2)
        dolares = str(dolares)
        print("tienes $"+dolares+" dolares")

    def Brazil():
        real = input("¿cuantos reales brasileños tienes? ")
        real = float(real)
        valor_dolar = 5.44
        dolares = real / valor_dolar
        dolares = round(dolares , 2)
        dolares = str(dolares)
        print("tienes $"+dolares+" dolares")