# Importar Librerias utiles

import time
from math import *
from Function_Metric import *
from playsound import playsound

def Ruido():
    playsound("./Sounds/Barra_Metal_Cayendo.mp3")
    return 0

Ruido()

N_pix=25

if (N_pix % 4) !=0:
        N_pix = N_pix + 4 - (N_pix % 4)

print(N_pix)


