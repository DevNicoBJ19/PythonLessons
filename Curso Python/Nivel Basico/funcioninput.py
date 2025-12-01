'''
funcion input: se utiliza para recibir datos del usuario a traves de la consola
La funcion input siempre devuelve un valor de tipo string, por lo que si se necesita otro tipo de dato, es necesario hacer un casting explicito despues de recibir el input


# Notas importantes:
# 1. Siempre que se utiliza input, el valor recibido es de tipo string.
# 2. Es necesario realizar un casting explicito si se requiere otro tipo de dato (int, float, bool, etc.).
# 3. Se pueden combinar funciones para procesar el input (por ejemplo, convertir a minusculas).
# 4. Usar nombres de variables descriptivos y evitar abreviaciones.

'''
#Ejemplo 1:
nombre = input("¿Cuál es tu nombre? ")  # Solicita al usuario que ingrese su nombre
print(f"Hola, {nombre}! Bienvenido/a.")  # Saluda al usuario usando el nombre ingresado

#age = input("¿Cuántos años tienes? ") #Aqui hay un error y es que la variable age sera de tipo string, hay que convertirla
age = int(input("¿Cuántos años tienes? "))  # Aqui encapsulamos el input en int() para convertir el valor ingresado a entero
print(f"En 20 años tendras {age + 20} años.")  # Muestra la edad ingresada por el usuario

#Obtener multiples valores
country, city = input("Ingresa tu país y ciudad separados por una coma: ").split(",")  # Solicita al usuario que ingrese país y ciudad separados por coma
print(f"Vives en {city}, {country}.")  # Muestra el país y ciudad ingresados





#Ejemplo 2:
nombre = input("Ingrese su nombre: ")  # Solicita al usuario que ingrese su nombre
edad = int(input("Ingrese su edad: "))  # Solicita al usuario que ingrese su edad y la convierte a entero
altura = float(input("Ingrese su altura en metros: "))  # Solicita al usuario que ingrese su altura y la convierte a float

# la explicacion detallada de esta variable es que primero se recibe el input como string, luego se convierte a minusculas con .lower()
# y finalmente se compara con "si" para obtener un booleano, es importante entender que despues de lower() sigue siendo un string pero con el == lo que hacemos
# es comparar si ese string es igual a "si", si es si, el resultado de la comparacion es True, si no, es False

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