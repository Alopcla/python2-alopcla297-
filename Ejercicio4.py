"""
4. Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable, y muestre por
pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa
corporal calculado redondeado con dos decimales. Para calcular IMC se divide el peso,
en kilos, por la altura, en metros al cuadrado.
"""

def calculaIMC(peso, altura):
    if(peso <= 0.0 or altura <= 0.0):
        print("Datos erróneos! No hay peso o altura inferior a 0")
    else:
        imc = peso / (altura**2)
        imc = round(imc, 2)
        print(f"Tu Indice de Masa Corporal es de {imc} imc.")

# MAIN
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Ahora, introduce tu altura en metros: "))
calculaIMC(peso, altura)

        