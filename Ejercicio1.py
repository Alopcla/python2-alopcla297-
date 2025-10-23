import array
"""
1. Escribir un programa que almacene en una lista los números del 1 al 100
y los muestre por pantalla en orden inverso separados por comas.
"""

# Funcion para invertir la lista, pasando por parametro la propia lista
def invertirLista(lista):
    lista.reverse()
    
# Funcion para crear una lista del 1 al 100
def crearLista(lista):
    for i in range(1, 100+1):
        lista.append(i) 
    
#
lista = []
crearLista(lista)
print(lista)
print()
invertirLista(lista)
print(lista)
