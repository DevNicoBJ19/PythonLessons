'''
Listas en Python:
Secuencias mutables de elementos
Pueden contener elementos de diferentes tipos
'''
import os
os.system("cls")
#Creacion de listas
print("Creacion de listas\n")

listas = [1,2,3,4,5,6] #lista de enteros
lista_texto = ["peras", "manzanas", "duraznos"] #listas de strings
lista_mixta = [1, "Hola", True, 3.14] #lista con que tipos de datos

#puedo escribir que tipo de datos tiene la lista, por ejemplo
#esta es la sintaxis para hacerlo:
lista_marcada: list[int] = [1,2,3,4,5,6]

#Si quisiera hacerlo con una lista dinamica o mixta esta seria la forma

lista_mixta2 : list[int | str | float | bool] = [1, "nicolas", 3.14, False] #dinamica enlistada
lista_vacia = []
lista_de_listas = [[1,2], [3,4]]
matrix = [[1,2], [3,4], [5,6]]

print(lista_mixta)
print(lista_mixta2)
print(lista_de_listas)
print(matrix)
print(lista_marcada)
print(lista_texto)
print(listas)

#Acceso a elementos por indice
lista_mixta = [1, "Hola", True, 3.14] #lista con que tipos de datos

print("Acceso a elementos de listas\n")
print(lista_mixta[0]) #Seria 1, porque el elemento 0 es el primero
print(lista_mixta[1]) #Seria hola
print(lista_mixta[-1]) # en negativo comienza desde el ultimo elemento
print(lista_mixta[-2]) #devuelve el True porque ahora vamos al reves

#Acceso a elementos de una matrix
matrix = [[1,2], [3,4], [5,6]]
print(matrix[1][0]) #Me muestra el 3

'''
SLICING (Rebanado) de listas
print(listas[desde:hasta])
'''
listas = [1,2,3,4,5,6,7,8,9,10] #lista de enteros
print(listas[1:4]) #podriamos creer que va hasta el numero 5, pero no incluye el ultimo valor, dice 1:4 pero imprime hasta la posicion anterior al 4
print(listas[:3]) #imprime del 1 al 3
print(listas[3:]) #posicion 3 es 4, hasta el final que es 5
print(listas[:]) #parece una copia de la misma lista

'''
print(listas[desde:hasta:paso]) El paso significa cada cuanto quiero saltar elementos
'''
print(listas[::2]) #devuelve indices pares [1, 3, 5, 7, 9]
print(listas[::-1]) #devuelve la lista invertida porque con el negativo va al reves [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

'''
MODIFICAR LISTAS
'''
listas[2] = 19 #variabilice en el espacio 2, que es el numero 3, y le puse el valor de 19
print(listas)

'''
AñADIR ELEMENTOS A LA LISTA
'''
#forma no eficiente porque la guarda en memoria y luego la añade
listas6 = [1,2,3]
listas6 = listas6 + [4,5,6] #aqui concatena a la misma lista
print(listas6)

#forma mas eficiente porque añade directamente
listas6 += [7,8,9]
print(listas6)


'''
EJERCICIOS
'''
# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
print(mensaje[7:])

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

numeros = [10, 20, 30, 40, 50]
numeros[0] = 50
numeros[4] = 10
print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes+ pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista = [1, 2, 3]
lista_duplicada = lista+ lista
print(lista_duplicada)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista = [10, 20, 30, 40, 50]
print(lista[2])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
'''
FORMA 1 (HARD CODE)
'''
lista_ultima = [1, 2, 3, 4, 5, 6]
primer_pedazo = lista_ultima[0:3]
inverso = primer_pedazo[::-1]
segundo_pedazo = lista_ultima[3:]
print(inverso + segundo_pedazo)

'''
FORMA 2 (MUCHO MEJOR)
'''
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida)


'''
FORMA 3 (NIVEL PERFECTO)
'''
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2

primera_mitad = lista[:mitad]
segunda_mitad = lista[mitad:]

lista_invertida = primera_mitad[::-1] + segunda_mitad
print(lista_invertida)