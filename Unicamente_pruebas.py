# Importar Librerias utiles

from Initial_Values import M, t_0, r_0, phi_0, theta_0, N_pix, Factor_Screen, Back_Im, constantes

import numpy as np
import time


def lit():
    lista=[]
    for i in range(100000000):
        lista.append(i)
    arr=np.array(lista)


def nump():
    arr=np.empty(100000000)
    for i in range(100000000):
        arr[i]=i

start=time.time()
lit()
print(time.time()-start)