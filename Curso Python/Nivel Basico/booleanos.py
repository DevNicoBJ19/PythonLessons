'''
Booleanos en Python
1. Los booleanos son un tipo de dato que puede tener dos valores: True (verdadero) o False (falso).
2. Se utilizan comúnmente en estructuras de control de flujo, como condicionales y bucles, para tomar decisiones basadas en condiciones lógicas.
3. Los operadores lógicos como and, or y not se utilizan para combinar o invertir valores booleanos.
# Ejemplo de uso de booleanos en Python
'''
#asi se importa una libreria, os es una libreria estandar de python, pero podemos instalar otras librerias externas
import os
os.system("cls") #limpia la consola en windows, en mac o linux se usa "clear"


print("\nEjemplo de Booleanos en Python:")
print(True)   # Imprime: True
print(False)  # Imprime: False

#Operadores de comparacion que devuelven booleanos
print("5 > 3:", 5 > 3)    # Imprime: True mayor que
print("2 == 4:", 2 == 4)  # Imprime: False igualdad
print("3 <= 3:", 3 <= 3)  # Imprime: True menor o igual que
print("7 != 7:", 7 != 7)  # Imprime: False desigualdad
print("10 < 5:", 10 < 5)  # Imprime: False menor que
print("8 >= 6:", 8 >= 6)  # Imprime: True mayor o igual que

#comparacion de cadenas
print("'apple' == 'apple':", 'apple' == 'apple')  # Imprime: True
print("'apple' != 'banana':", 'apple' != 'banana')  # Imprime: True

'''
(comparacion lexicografica) lexicografica significa que se compara letra por letra segun el orden alfabetico
ejemplo:
'manzana' > 'banana'  # True, porque 'm' viene despues de 'b' en el alfabeto
'abc' < 'abd'        # True, porque 'c' viene antes de 'd' en el alfabeto
'cat' < 'catalog'    # True, porque 'cat' es una subcadena de 'catalog'
'hello' > 'Hello'    # True, porque las letras minusculas tienen un valor ASCII mayor que las mayusculas
'zebra' > 'apple'    # True, porque 'z' viene despues de 'a' en el alfabeto
'123' < '124'        # True, porque '3' es menor que '4'
'abc' < 'abcd'      # True, porque 'abc' es una subcadena de 'abcd'
'same' == 'same'    # True, porque ambas cadenas son iguales
'Test' != 'test'    # True, porque las cadenas son diferentes debido a la mayuscula

'''
#ejemplos de comparacion lexicografica
print("manzana' > 'banana':", 'manzana' > 'banana')  # Imprime: True


#Operadores Logicos: and, or, not
print("\nOperadores Lógicos:")
print("True and False:", True and False)  # Imprime: False
print("True or False:", True or False)    # Imprime: True
print("not True:", not True)                # Imprime: False
print("not False:", not False)              # Imprime: True
print("True and True:", True and True)    # Imprime: True
print("False or False:", False or False)  # Imprime: False


#Tablas de la verdad
print("\nTabla de la Verdad:")
print("A\tB\tA and B\tA or B\tnot A")
print("True\tTrue\t", True and True, "\t", True or True, "\t", not True)
print("True\tFalse\t", True and False, "\t", True or False, "\t", not True)
print("False\tTrue\t", False and True, "\t", False or True, "\t", not False)
print("False\tFalse\t", False and False, "\t", False or False, "\t", not False)

#tabla de la verdad AND
print("\nTabla de la Verdad AND:")
print("A\tB\tA and B")
print("True\tTrue\t", True and True)
print("True\tFalse\t", True and False)
print("False\tTrue\t", False and True)
print("False\tFalse\t", False and False)

#tabla de la verdad OR
print("\nTabla de la Verdad OR:")
print("A\tB\tA or B")
print("True\tTrue\t", True or True)
print("True\tFalse\t", True or False)
print("False\tTrue\t", False or True)
print("False\tFalse\t", False or False)

#tabla de la verdad NOT
print("\nTabla de la Verdad NOT:")
print("A\tnot A")
print("True\t", not True)
print("False\t", not False)



# Uso de booleanos en condicionales
es_mayor = True
if es_mayor:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")