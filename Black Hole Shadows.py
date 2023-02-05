# Importar Librerias utiles
import sympy as sp
import math
import random

import Angle_to_Momentum
from Angle_to_Momentum import *
import Solving_Kerr_with_Christoffel
from Solving_Kerr_with_Christoffel import *

# Parametros del Agujero Negro (Masa, Spin, Carga electrica y Magnetica, etc)
M=1
a=0
param=(M,a)

# Posicion del Observador y Condiciones Iniciales
t_0=0
r_0= 5*M
phi_0=0
theta_0= math.pi/4
coords_0=(t_0, r_0, phi_0, theta_0)

# Numero de Pixeles en un lado, el numero de pixeles total será, N_pix * N_pix
N_pix=100


# Lo de arriba lo debe de dar el usuario, a partir de aqui, es el programa

L=4*3*M #¿no se como de grande tiene que ser, supongo que funcion de r_0?¿Quizá, cambiarlo a que ejecute Geodesic_Chris para un caso de un foton radial, y segun donde este el horizonte de eventos?
paso=L/N_pix

for i in range(N_pix):
    for j in range(N_pix): 
            x=i*paso
            y=j*paso
            list_momentum=Screen_to_Momentum(x, y, *coords_0, *param)
            tupla_momentum=(list_momentum[0], list_momentum[1], list_momentum[2], list_momentum[3])
            In_or_out=Geodesic_Chris(*coords_0, *tupla_momentum , *param)

            if In_or_out==1:
                0
                # Cae al agujero negro
            elif In_or_out==0:
                0
                # No cae al agujero negro
            else:
                print('Error')



            
# rnd=random.random()    Usar esto para cuando haga un montecarlo



