# Importamos la galeria.
import random

# Le pedimos a la computadora que nos genere un numero aleatorio

numeros = [1,2,3,4,5,6,7,8,9,10]
numero = random.choice(numeros)

print("He generado un numero del 1 al 10.")

# El usuario debera adivinar el numero

mensaje_usuario = ("Intente adivinar el numero generado aleatoriamente.")

print(mensaje_usuario)

while True:
    try:
        respuesta = int(input("Su numero a elegir será: "))
        
    except ValueError:
        print("Debes ingresar un numero válido.")
        continue

# Verificamos si el número es correcto

    if respuesta == numero:
        print("¡Felicidades! Acertaste.")
        break
    elif respuesta < numero:
        print("El número es mayor.")
    else:
        print("El número es menor.")




