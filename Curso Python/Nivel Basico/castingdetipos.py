'''
Casting de tipos en Python:
En Python, el casting de tipos se refiere a la conversión explícita de un tipo de dato a otro.
Esto es útil cuando se necesita realizar operaciones entre diferentes tipos de datos o cuando se desea
asegurar que una variable tenga un tipo específico.

# Notas importantes:
# 1. Al convertir de float a int, se trunca la parte decimal (no se redondea).
# 2. Al convertir cadenas a números, la cadena debe representar un valor numérico válido.
# 3. El casting puede generar errores si la conversión no es posible (por ejemplo, convertir "abc" a int).
'''

#conversion de tipos
#se le añade el int y luego se encapsula el string "100" para convertirlo a entero
print(int("100")+2)
print(2+int("100"))

# Ejemplos de casting de tipos en Python
# Convertir a entero
entero_desde_flotante = int(10.99)# Convierte float a int, resultado: 10
entero_desde_string = int("20")         # Convierte str a int, resultado: 20

#ejemplo de como python interpreta el casting automatico en operaciones

# print('100' + 2)  # Concatenacion de string y numero da error
#para hacer que no de error, se hace casting del string a int
entero_desde_string_corregido = int("100") + 2  # Resultado: 102
print(entero_desde_string_corregido)
# print(2 + '100')  # Concatenacion de numero y string da error
#para hacer que no de error, se hace casting del int a str
entero_desde_string_corregido_2 = str(2) + "100"  # Resultado: "2100"
print(entero_desde_string_corregido_2)

# Convertir a flotante
flotante_desde_entero = float(10)       # Convierte int a float, resultado: 10.0
flotante_desde_string = type(float("15.75"))  # Convierte str a float, resultado: 15.75
#este print dara False porque es texto vacio
print(bool(""))
#este print dara True porque es texto pero tiene algo dentro
print(bool(" "))

#el siguiente caso ocurre porque al redondear 2.5, python redondea al numero par mas cercano
#la explicacion a redondear al par mas cercano es para evitar sesgos en grandes cantidades de datos

print(round(2.5)) #esto redondea al numero par mas cercano, en este caso 2
print(round(3.5)) #esto redondea al numero par mas cercano, en este caso 4

# Convertir a cadena
string_desde_entero = str(100)          # Convierte int a str, resultado: "100"
string_desde_flotante = str(12.34)      # Convierte float a str, resultado: "12.34"

# Convertir a booleano
booleano_desde_entero = bool(1)         # Convierte int a bool, resultado: True
booleano_desde_string = bool("")        # Convierte str a bool, resultado: False

# Ejemplos de casting INCORRECTO (descomentar para ver errores)
#entero_desde_string_invalidado = int("abc")  # Error: ValueError, es imposible pasar un texto a numero
#flotante_desde_string_invalidado = float("xyz")  # Error: ValueError, es imposible pasar un texto a numero decimal
#flotante_desde_string_valido = float("123.456") # Convierte str a float, resultado: 123.456
#booleano_desde_lista = bool([1, 2, 3])  # Convierte lista a bool, resultado: True (no es un error, pero es un caso especial) no tiene sentido convertir una lista a booleano, a menos que sea vacia o no vacia
# Nota: En Python, el casting de tipos se realiza mediante funciones integradas como int(), float(), str(), y bool().
