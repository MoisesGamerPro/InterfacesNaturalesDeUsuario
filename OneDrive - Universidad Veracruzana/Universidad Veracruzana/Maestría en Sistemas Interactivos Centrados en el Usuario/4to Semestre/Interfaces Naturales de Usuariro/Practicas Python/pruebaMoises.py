print("¡Hola, Mundo!")

# Ejemplo de variables y tipos de datos
edad = 25
nombre = "Juan"
altura = 1.75

# Ejemplo de estructuras de control de flujo
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

for i in range(5):
    print(i)

# Ejemplo de función
def saludar(nombre):
    print("¡Hola, " + nombre + "!")

saludar("Ana")

# Ejemplo de lista y diccionario
colores = ["rojo", "verde", "azul"]
persona = {"nombre": "Carlos", "edad": 30}

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No puedes dividir por cero.")

# Ejemplo de importación de biblioteca
import math

print(math.sqrt(25))
