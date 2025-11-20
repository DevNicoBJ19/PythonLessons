'''
Tipos de datos en Python: Teoria
Los tipos de datos en Python son las diferentes categorías de valores que se pueden utilizar en un programa.
Algunos de los tipos de datos mas comunes en Python son:
1. Numericos:   int (enteros), float (numeros de punto flotante), complex (numeros complejos)
2. Secuencias:  str (cadenas de texto), list (listas), tuple (tuplas), range (rangos)
3. Mapeos:      dict (diccionarios)
4. Conjuntos:   set (conjuntos), frozenset (conjuntos inmutables)
5. Booleanos:   bool (valores True o False)
6. Binarios:    bytes (secuencias de bytes), bytearray (arreglos de bytes mutables), memoryview (vista de memoria)
Cada tipo de dato tiene sus propias caracteristicas y operaciones asociadas. Por ejemplo, los numeros pueden ser sumados o multiplicados,
mientras que las cadenas de texto pueden ser concatenadas o divididas. Las listas y tuplas son colecciones ordenadas de elementos,
mientras que los diccionarios son colecciones de pares clave-valor.
Los tipos de datos en Python son dinamicos, lo que significa que no es necesario declarar el tipo de una variable antes de usarla.
'''
# Ejemplos de tipos de datos en Python
# Numericos
#los int son numeros enteros, los float son numeros decimales y los complex son numeros complejos
entero = 10               # int
entero_negativo = -5      # int negativo
entero_grande = 12345678901234567890  # int grande
entero_cero = 0          # int cero

#los float son numeros de punto
flotante = 10.5          # float decimal
flotante_negativo = -3.14 # float negativo
flotante_cientifico = 1.5e3 # float en notacion cientifica significa 1.5 * 10^3
flotante_cero = 0.0      # float cero

#los complex son numeros complejos que tienen una parte real y una imaginaria
complejo = 3 + 4j        # complex
complejo_negativo = -2 - 5j # complex negativo
complejo_cero = 0j       # complex cero

# Secuencias
#strings son cadenas de texto
cadena = "Hola, Mundo!"   # str
cadena_simple = 'Python es genial'  # str con comillas simples
cadena_multilinea = """Esta es una cadena
multilinea en Python."""  # str multilinea
cadena_vacia = ""         # str vacia

#las listas son colecciones ordenadas que pueden contener elementos de diferentes tipos, las listas son aquellos que se definen con corchetes [], contienen elementos separados por comas
lista = [1, 2, 3, 4, 5]   # list
lista_mixta = [1, "dos", 3.0, True]  # list mixta

#la diferencia entre listas y tuplas es que las tuplas son inmutables (no se pueden modificar)
tupla = (1, 2, 3)         # tuple
tupla_mixta = (1, "dos", 3.0, False)  # tuple mixta

#rango es una secuencia inmutable de numeros enteros, por ejemplo para bucles funciona bien
rango = range(0, 10)      # range
rango_paso = range(0, 10, 2)  # range con paso de 2 que significa que va de 0 a 10 saltando de 2 en 2
rango_negativo = range(10, 0, -1) # range con paso negativo que va de 10 a 1
rango_cero = range(0)     # range vacio

# Mapeos
#un diccionario es una coleccion de pares clave-valor, lo que signfica que cada valor se accede mediante una clave unica
diccionario = {"clave1": "valor1", "clave2": "valor2"}  # dict
diccionario_vacio = {}    # dict vacio
diccionario_mixto = {1: "uno", "dos": 2, 3.0: True}  # dict mixto significa que las claves y valores pueden ser de diferentes tipos

# Conjuntos
#conjunto es una coleccion no ordenada de elementos unicos, ejemplo: no hay elementos duplicados y no tienen un orden especifico
conjunto = {1, 2, 3, 4, 5}          # set
conjunto_vacio = set()            # set vacio
conjunto_mixto = {1, "dos", 3.0, False}  # set mixto

#inmutables signidica que no se pueden modificar despues de su creacion
conjunto_inmutable = frozenset([1, 2, 3])  #
conjunto_inmutable_vacio = frozenset()  # frozenset vacio
conjunto_inmutable_mixto = frozenset([1, "dos", 3.0, True])  # frozenset mixto

# Booleanos
#los booleanos representan valores de verdad: True (verdadero) o False (falso)
booleano = True                     # bool
booleano_falso = False              # bool falso
booleano_desde_entero = bool(1)   # bool desde entero (True)
booleano_desde_cadena = bool("")   # bool desde cadena vacia (False)
booleando_logico = 10 > 5    # bool desde operacion logica (False)

# Binarios
#Secuencias de bytes son datos binarios, lo que significa que son datos en formato bruto
secuencia_bytes = b"Hola"          # bytes
#un arreglo de bytes es una secuencia mutable de bytes, lo que significa que se pueden modificar despues de su creacion
arreglo_bytes = bytearray(b"Hola")  # bytearray
#estos vista memoria permiten acceder a los datos binarios sin copiarlos
vista_memoria = memoryview(b"Hola")  # memoryview

#nontype: este tipo de dato especial representa la ausencia de valor, ejemplo cuando una funcion no retorna nada
#none es un objeto unico en Python que indica la ausencia de valor o un valor nulo
nulo = None                       # NoneType

# Imprimir los tipos de datos
print(type(entero))
print(type(flotante))
print(type(complejo))
print(type(cadena))
print(type(lista))
print(type(tupla))
print(type(rango))
print(type(diccionario))
print(type(conjunto))
print(type(conjunto_inmutable))
print(type(booleano))
print(type(secuencia_bytes))
print(type(arreglo_bytes))
print(type(vista_memoria))
print(type(nulo))