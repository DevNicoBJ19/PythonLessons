'''
funcion input: se utiliza para recibir datos del usuario a traves de la consola
La funcion input siempre devuelve un valor de tipo string, por lo que si se necesita otro tipo de dato, es necesario hacer un casting explicito despues de recibir el input


# Notas importantes:
# 1. Siempre que se utiliza input, el valor recibido es de tipo string.
# 2. Es necesario realizar un casting explicito si se requiere otro tipo de dato (int, float, bool, etc.).
'''

#Ejemplo:
nombre = input("Ingrese su nombre: ")  # Solicita al usuario que ingrese su nombre
edad = int(input("Ingrese su edad: "))  # Solicita al usuario que ingrese su edad y la convierte a entero
altura = float(input("Ingrese su altura en metros: "))  # Solicita al usuario que ingrese su altura y la convierte a float
# la explicacion detallada de esta variable es que primero se recibe el input como string, luego se convierte a minusculas con .lower() y finalmente se compara con "si" para obtener un booleano
es_mayor = input("¿Es mayor de edad? (si/no): ").lower() == "si"
# Solicita al usuario que indique si es mayor de edad y convierte la respuesta a booleano
# Mostrar los datos ingresados
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura} metros")
print(f"Es mayor de edad: {es_mayor}")

#ejemplo 2
print('como te llamas?\n')  # imprime la pregunta y un salto de linea para que en la consola el cursor quede en la siguiente linea
nombre_usuario = input()  # recibe el input del usuario y lo guarda en la variable nombre_usuario
print(f'Hola {nombre_usuario}, bienvenido!')  # imprime un mensaje de bienvenida