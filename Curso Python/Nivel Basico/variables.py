'''
Variables en Python: Son aquellas que almacenan datos para su uso posterior, como cajas que guardan información.
para asignar una variable, se utiliza el signo igual (=).

recordemos que python es de tipado dinamico, por lo que no es necesario declarar el tipo de variable, se determina en tiempo de ejecucion
un jemplo de tipado estatico seria en lenguajes como Java o C#, donde se debe declarar el tipo de variable al momento de su creacion

Convenciones de nombres de variables en python:
# 1. Usar letras minúsculas y guiones bajos para separar palabras (snake_case) ejemplo: mi_variable_ejemplo
# 2. No usar palabras reservadas de Python (como 'if', 'for', 'while', etc.) ejemplo: 'if' = 10 #esto dara error
# 3. Los nombres de variables deben comenzar con una letra o un guion bajo (_), no con un número ejemplo: 1variable = 10 #esto dara error
# 4. Ser descriptivo con los nombres de las variables para mejorar la legibilidad del código. ejemplo: edad_usuario en lugar de e o x
'''
#Ejemplos de variables en Python

my_name = "Nicolas"  # Variable de tipo string
print("Hola, mi nombre es " + my_name)
my_age = 25          # Variable de tipo entero
print(my_age)
#aqui a pesar de ser la misma variable, pero con diferente valor, python la interpreta como la ultima asignacion
my_age = 35
# print("hola mi edad es " + my_age) #esto dara error porque se esta intentando concatenar un string con un entero


my_height = 1.75    # Variable de tipo float
print(type(my_height))

my_height = "1.75 metros"  # Ahora es una variable de tipo string
print(type(my_height))

#tipado fuerte: significa que python no realiza conversiones automaticas entre tipos de datos, por ejemplo, no se puede sumar un string con un entero sin hacer un casting explicito
#ejemplo de tipado fuerte

# Esto generaria un error de tipo TypeError

#es mejor usar f strings para evitar estos errores
print(f"Mi edad es {25+100}")

#si declaro una variable toda en mayusculas, se interpreta como una constante, aunque python no tiene constantes reales
PI = 3.1416
print(PI)

