
# ESTEGANOGRAFIA: imagen30.jpg "Al Fascismo no se le discute, se le destruye." Buenaventura Durruti

import queue
from queue import PriorityQueue
import operator
import os

letras = "abcdefghijklmnñopqrstuvwxyz"
letrasPrioridad = "1:e | 2:a | 3:o | 4: l | 5:s \n--------------------------\n6:n | 7:d | 8:r | 9:u | 10:i \n--------------------------\n11:t | 12:c | 13:p | 14:m | 15:y | \n--------------------------\n16:q | 17:b | 18:h | 19:g | 20:f \n--------------------------\n21:v | 22:j | 23:ñ | 24:z | 25:x \n-------------\n26:k | 27:w"
enum_letras = {}

for letra in letras:
    enum_letras[letra] = 0


f = open("/home/hugo/visualCodeProjects/sgssi_cifrado_I/mensaje.txt", "r")
mensaje = f.read().lower()

for letra in mensaje:
    if letra in enum_letras:
        enum_letras[letra] += 1

letras_sort = sorted(enum_letras.items(), key=operator.itemgetter(1), reverse=True)

x = " "
par_letras = {}
while True:
    print("Tabla de prioridad: \n")
    print(letrasPrioridad)
    print("\n###########################################################\n")
    print("Tabla de frecuencias: \n")
    print(letras_sort)
    print("\n###########################################################\n")
    print("Pares de letras asociadas: \n")
    print(par_letras)
    print("\n###########################################################")
    print(mensaje)
    print("###########################################################")

    letraSus = input("Escribe la letra que quieres sustituir: " )
    letraNew = input("Escribe la letra por la que quieres sustituir: ")
    par_letras[letraSus] = letraNew
    mensaje = mensaje.replace(letraSus, letraNew.upper())
    x = input("Si quiere salir escriba 'y' o 's' : ")
    if x == "y" or x == "s":
        print(mensaje)
        break

