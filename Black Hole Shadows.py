# Importar Librerias utiles
import numpy as np
import sympy as sp
import math
import random

# Parametros del Agujero Negro (Masa, Spin, Carga electrica y Magnetica, etc)
M=1
a=0

# Posicion del Observador y Condiciones Iniciales
t_0=0
r_0= 5*M
phi_0=0
theta_0= math.pi/4

# Numero de Pixeles en un lado, el numero de pixeles total será, N_pix * N_pix
N_pix=100

# rnd=random.random()    Usar esto para cuando haga un montecarlo
