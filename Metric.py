# Importar Librerias utiles
import numpy as np
import sympy as sp
import math

from sympy import*

M=symbols("M")
t,r,theta,phi=symbols("t,r,theta,phi")

g00=-(1-2*M/r)
g01=0
g02=0
g03=0
g10=0
g11=1/(1-2*M/r)
g12=0
g13=0
g20=0
g21=0
g22=r**2
g23=0
g30=0
g31=0
g32=0
g33=r**2*sin(theta)**2

G= np.array([[g00,g01,g02,g03],[g10,g11,g12,g13],[g20,g21,g22,g23],[g30,g31,g32,g33]])
