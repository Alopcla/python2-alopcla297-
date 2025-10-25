from random import randint
"""
3. Pide al usuario un número. Crea una lista de palabras, que se irán pidiendo al usuario.
La cantidad de palabras que se pidan será el número que se introdujo. Muestra la lista.
A continuación, pide al usuario una nueva palabra y cambia la palabra que está posicionada
en la mitad de la lista por la nueva palabra. Muestra la lista de nuevo. Pide al usuario
una palabra y muestra un mensaje indicando si esa palabra está o no en la lista.
Muestra de entre toda la lista una palabra de forma aleatoria.
"""
# FUNCIONES
def elegirPalabraRandom(lista):
    pos = randint(0, len(lista))
    
    palabra = lista[pos]
    
    return palabra

def estaEnLista(lista, palabra):
    encontrado = False
    pos = 0
    
    while(pos < len(lista)):
        if(lista[pos] == palabra):
            encontrado = True
        pos += 1
        
    if(encontrado):
        print(f"La palabra '{palabra}' SI se encuentra en dicha lista.")
    else:
        print(f"La palabra '{palabra}' NO se encuentra en dicha lista.")
        
def introducirPalabra(lista, palabra):
    longitud = len(lista)
    mitadLista = lista[int(longitud/2)]
    
    if(longitud == 1 or longitud == 0 or longitud == 2):
        print("No se puede introducir en mitad de la lista porque solo contiene elementos pares o ningun elemento...")
    elif(longitud > 2 and not(mitadLista == 0)):
        lista[int(longitud/2)] = palabra        
        
def mostrarLista(lista):    
    return print(lista)

# PRINCIPAL FUNCION
def listadoPalabras():
    lista = []
    longitud = int(input("Introduce un numero: "))
    
    if(longitud != 0):
        while (len(lista) < longitud):
            palabra = input("Introduce una palabra: ")
            lista.append(palabra.lower())
        mostrarLista(lista)
    
        nuevaPalabra = input("Introduce una nueva palabra: ")
        introducirPalabra(lista, nuevaPalabra.lower())
        mostrarLista(lista)
        
        otraPalabra = input("Palabra a buscar en la lista: ")
        estaEnLista(lista, otraPalabra.lower())
        
        palabraRand = elegirPalabraRandom(lista)
        print(f"La palabra aleatoria elegida es '{palabraRand.lower()}'")
        
    else:
        print("No se puede introducir palabras ya que la lista contiene cero elementos...")
        
# MAIN
listadoPalabras()