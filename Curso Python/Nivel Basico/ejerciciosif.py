import os
os.system("cls")

'''
Ejercicios
'''

#1.Escribe un programa que solicite la edad del usuario y muestre si es mayor de edad (≥18) o menor de edad

edad = int(input("Ingrese su edad: \n"))

if edad >=18:
    print("Es mayor de edad")
else:
    print("es menor de edad")

#2. Pide al usuario un número entero y determina si es par o impar usando el operador módulo.

numero = int(input("Escribe el numero: \n"))

if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es inpar")

#3. Solicita dos números y muestra si son iguales o diferentes

numero_uno = int(input("digita el primer numero: \n"))
numero_dos = int(input("digita el segundo numero: \n"))

if numero_uno == numero_dos:
    print("Los numeros son iguales")
else:
    print("Los numeros son diferentes")


#4. Pide un número y determina si es positivo, negativo o cero.
numero = int(input("digita el numero: \n"))

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("el numero es cero")

#5.Ingresa una nota (0-100) y muestra la calificación: A (90-100), B (80-89), C (70-79), D (60-69), F (<60).

nota = int(input("Ingresa la nota"))

if nota >= 90:
    print("Calificacion: A")
elif nota >=80:
    print("Calificacion: B")
elif nota >=70:
    print("Calificacion: C")
elif nota >=60:
    print("Calificacion: D")
else:
    print("Calificacion: F")
#6 Registra tres notas de un alumno, calcula el promedio y muestra si está aprobado (promedio ≥ 11) o desaprobado

nota_uno = int(input("Ingresa la nota 1: \n"))
nota_dos = int(input("Ingresa la nota 2: \n"))
nota_tres = int(input("Ingresa la nota 3: \n"))

nota_final = (nota_uno + nota_dos + nota_tres) / 3
print(f"Nota final {nota_final}")
if nota_final >= 11:
    print("Aprobado")
else:
    print("La pecheo")


#7.  calculadora que pida dos números y una operación (+, -, *, /) y muestre el resultado.

numero_uno = int(input("ingrese el primer numero: \n"))
numero_dos = int(input("ingrese el segundo numero: \n"))
operation_type = input("Operación (+, -, *, /): ")

if operation_type == ("+"):
    resultado_suma = numero_uno + numero_dos
    print(resultado_suma)
elif operation_type == ("-"):
    resultado_resta = numero_uno - numero_dos
    print(resultado_resta)
elif operation_type == ("*"):
    resultado_multi = numero_uno * numero_dos
    print(resultado_multi)
else:
    resultado_div = numero_uno / numero_dos
    print(resultado_div)