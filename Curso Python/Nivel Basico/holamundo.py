'''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Python es un lenguaje de programación interpretado, interactivo y orientado a objetos. Fue creado por Guido van Rossum
y lanzado por primera vez en 1991. Python es conocido por su sintaxis clara y legible, lo que facilita el aprendizaje
y la escritura de código.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Caracteristicas principales de Python:
1. Sintaxis clara y legible: Python utiliza una sintaxis que enfatiza la legibilidad del código, lo que facilita su comprensión.
2. Tipado dinámico: No es necesario declarar el tipo de una variable; Python lo determina automáticamente en tiempo de ejecución.
3. Interpretado: Python se ejecuta línea por línea, lo que facilita la depuración y el desarrollo interactivo.
4. multiparadigma: Soporta programación orientada a objetos, programación funcional y programación imperativa.
5. Amplia biblioteca estándar: Python viene con una extensa biblioteca estándar que proporciona módulos y funciones para diversas tareas.
6. Multiplataforma: Python es compatible con múltiples sistemas operativos, como Windows, macOS y Linux.
7. Lenguaje de alto nivel: Python abstrae muchos detalles del hardware, lo que permite a los desarrolladores centrarse en la lógica del programa.
8. se puede usar en desarrollo web, ciencia de datos, inteligencia artificial, automatización, entre otros.
9. Es un lenguaje de proposito general, lo que significa que se puede utilizar para una amplia variedad de aplicaciones.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Filosofia de Python (The Zen of Python):
4 citas que resumen los principios de diseño de Python:
1. la legibilidad cuenta.
2. construccion de prototipos rapidos es mejor que construccion lenta de programas complejos.
3. la simplicidad es mejor que la complejidad.
4. sintaxis comprensible para humanos, no para maquinas.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
interprete interactivo de Python:
es una herramienta que permite a los desarrolladores escribir y ejecutar codigo Python de manera interactiva.
Proporciona un entorno donde se pueden probar fragmentos de codigo, experimentar con funciones y explorar
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
#Ejemplo basico de Python

#modulo print: se utiliza para mostrar mensajes en la consola
#Los comentarios en python se hacen con el simbolo numeral

#Una funcion es un bloque de codigo reutilizable que realiza una tarea especifica

print("Hola Mundo con comilla doble")
print('Hola Mundo con comilla simple')

#imprime 3 argumentos separados por espacio
#la coma automaticamente agrega un espacio entre los argumentos al imrpimir
print("Python", "es", "genial")

#sep: parametro que define el separador entre los argumentos de la funcion
print("Python", "es", "genial", sep="-") #cambia el separador por defecto (espacio) por un guion

#end: parametro que define el caracter que se imprime al final de la linea
print("Python", "es", "la verga", end="!!")#Esta linea se imprime con la de abajo, pero la de abajo hace el salto de linea
print("Python", "es", "la verga", end="\n") #cambia el final de linea por un salto de linea explicito

print("esto se va a imprimir", end=" ")#Con este end cambiamos el salto de linea por un espacio
print("en la misma linea")# asi que a pesar que sean dos print, se imprimen en la misma linea