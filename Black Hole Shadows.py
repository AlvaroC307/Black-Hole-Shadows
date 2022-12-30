# Importar Librerias utiles
import numpy as np
import sympy as sp
import math

# Parametros del Agujero Negro (Masa, Spin, Carga electrica y Magnetica, etc)
M=1
a=0
Qe=0
Qm=0

# Posicion del Observador y Condiciones Iniciales
r_0= 0
theta_0= 0

# Numero de Pixeles en un lado, el numero de pixele total será, N_pix * N_pix
N_pix=100