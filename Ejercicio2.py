from random import randint
"""
2. Generar un número aleatorio de números aleatorios (de entre 1 y 20)
y añadirlos a una lista. Mostrar la lista y el número de elementos de la lista.
"""

def numerosRandom(lista):
    long = randint(1, 20)
    
    for _ in range(1, long):
        num = randint(1, 20)
        lista.append(num)
        
    return lista

lista = []
numerosRandom(lista)
print(lista)
numElementos = len(lista)
print(f"El número de elementos de la lista es de {numElementos}")