'''
Condicionales en Python:
Los condicionales permiten ejecutar diferentes bloques de código según ciertas condiciones.
En Python, los condicionales se implementan utilizando las palabras clave if, elif y else
# Notas importantes:
# 1. La indentación es crucial en Python para definir bloques de código.
# 2. Las condiciones pueden combinarse usando operadores lógicos (and, or, not).
# 3. Se pueden anidar condicionales dentro de otros condicionales.

'''
#asi se importa una libreria, os es una libreria estandar de python, pero podemos instalar otras librerias externas
import os
os.system("cls") #limpia la consola en windows, en mac o linux se usa "clear"

# Ejemplo de condicionales en Python
print("Sentencia Simple condicional:")

edad = 18
if edad >= 18:
    print("Eres mayor de edad.")

edad = 15
if edad >= 18:
    print("Eres menor de edad.")

#condicional con else
edad = 17
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#bifurcacion con elif (entre mas bifurcaciones, se usan mas elif, lo que hace que se complique la lectura del codigo, por lo que es recomendable no abusar de ellos)

edad = 19
if edad >= 18:
    print("Eres mayor de edad")
elif edad == 17:
    print("Tienes 17 años")
else:
    print("Eres menor de 17 años")


#ejemplo 2
#pedimos por consola con input, lo volvemos un int porque eso es lo que recibiremos en consola
nota = int(input("Ingresa tu nota (0-5): "))

if nota >= 5:
    print("Aprobado con excelente nota")
elif nota >= 4:
    print("Aprobado con buena nota")
elif nota >= 3:
    print("Aprobado con nota regular")
else:
    print("Reprobado")

#ejemplo 3
#condiciones multiples con operadores logicos

if edad >= 18 and edad < 65:
    print("Eres un adulto, puedes conducir y trabajar.")
else:
    print("No eres un adulto en edad laboral.")


#ejemplo 4
edad = 20
licence = False

if edad >= 18 and licence:
    print("Puedes conducir.")
else:
    print("No puedes conducir.")

#Matematica discreta en condicionales
#la tabla es la siguiente
'''
and | or | not
True | True | False
True | False | False
True | True | False
False | True | True
False | False | True
False | True | True
'''
#El or lo que dice es que si alguna de las dos condiciones es verdadera, entonces la condicion completa es verdadera
if edad >= 18 or licence:
    print("Puedes conducir o tienes licencia.")
else:
    print("Paga al policia y te puedes ir.")

#El not invierte el valor de la condicion
its_weekend = True
if not its_weekend:
    print("Es dia laboral.")


#Anidar condicionales

edad = 18
dinero = True

#No muy recomendable anidar condicionales, pero es posible, su dificultad de lectura aumenta con la anidacion
#Tener cuidado con la tabulacion
if edad >= 18:
    if dinero:
        print("Puedes salir a divertirte.")
    else:
        print("No tienes dinero para salir.")
else:
    print("Eres menor de edad, no puedes salir.")

#Mismo ejemplo pero mas facil de leer usando elif
if edad < 18:
    print("Eres menor de edad, no puedes salir.")
elif dinero:
    print("Puedes salir a divertirte.")
else:
    print("No tienes dinero para salir.")


#Condicionales para booleanos
#para este ejemplo, si la variable numero es diferente de cero, se interpreta como True, si es cero, se interpreta como False
numero = 5

if numero:
    print("El numero es diferente de cero.")
else:
    print("El numero es cero.")


numero = 0
if numero:
    print("El bucle no entrara aqui nunca.")
else:
    print("El numero es cero, por lo que se interpreta como False.")


nombre = "Nicolas" #Si este string estuviera vacio, se interpretaria como False

if nombre:
    print("El nombre no esta vacio.")
else:
    print("El nombre esta vacio.")