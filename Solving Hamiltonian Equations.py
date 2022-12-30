# Importar Librerias utiles
import numpy as np
import sympy as sp
import math

# Importar otros ficheros de la carpeta

import Metric
from Metric import*

# Este codigo se tiene que ejecutar mucho, para cada resolucion de las ecuaciones

# Parametros del Agujero Negro (Masa, Spin, Carga electrica y Magnetica, etc)
M=1
a=0
# Condiciones "Iniciales" (finales) del foton al llegar a la pantalla
# Los momentos son una-formas, es decir, indices bajados
t_0=0.0
r_0=0.0
theta_0=0.0
phi_0=0.0
p_t_0=0.0
p_r_0=0.0
p_theta_0=0.0
p_phi_0=0.0

# Calculo de las Constantes del Movimiento para ciertas condiciones "iniciales"
E=-p_t_0
L_z=p_phi_0
Q=(p_theta_0)**2-(a*E*math.cos(theta_0))**2+(L_z/math.tan(theta_0))
mu2=0 # Como son para geodesicas luminosas siempre se tomara mu^2=0, esto ya se ha tenido en cuenta en las
# ecuaciones de hamilton siguientes, y los terminos proporcionales a mu no existen 


# Definicion de Delta y rho^2

def Delta(r):
    return r**2+a**2-2*M*r


def rho2(r,theta):
    return r**2+(a*math.cos(theta))**2


# Definicion del Hamitoniano

def H(r,theta,p_r,p_theta):
    sumando1=(a*L_z-(r**2+a**2)*E)**2/(Delta(r))
    sumando2=(L_z-a*E*(math.sin(theta))**2)**2/(math.sin(theta))**2
    return (Delta(r)*p_r**2+p_theta**2+sumando1+sumando2)/(2*rho2(r,theta))


# Definir las 6 funciones que se van a integrar

def t_punto(r,theta):
    return ((Delta(r)*rho2(r,theta)+2*M*r*(r**2+a**2))/(Delta(r)*rho2(r,theta)))*E-(2*M*r*a/(Delta(r)*rho2(r,theta)))*L_z


def phi_punto(r,theta):
    return ((2*M*r*a)/(Delta(r)*rho2(r,theta)))*E+((rho2(r,theta)-2*M*r)/(Delta(r)*rho2(r,theta)*(math.sin(theta))**2))*L_z 


def p_theta_punto(r,theta,p_r,p_theta):
    sumando1=(-2*r*E)*(a*L_z-(r**2+a**2)*E)/Delta(r)
    sumando2=(-2*(r-M)*(a*L_z-(r**2+a**2)*E)**2)/(Delta(r))**2
    return (2*r*H(r,theta,p_r,p_theta))/(rho2(r,theta))-((r-M)*p_r**2-sumando1+sumando2)/(rho2(r,theta))


def p_r_punto(r,theta,p_r,p_theta):
    sumando1=(-a*E*(L_z-a*E*(math.sin(theta))**2))/(math.sin(theta))**2
    sumando2=((L_z-a*E*(math.sin(theta))**2)**2)/(math.sin(theta))**4
    return (-math.sin(2*theta)/rho2(r,theta))*(H(r,theta,p_r,p_theta)+sumando1-sumando2)

def theta_punto(r,theta,p_theta):
    return (p_theta/rho2(r,theta))


def r_punto(r,theta,p_r):
    return ((Delta(r)*p_r)/rho2(r,theta))


# Metodo de RK4 para 6 ecuaciones diferenciales de primer orden (p_t y p_phi están ya calculadas al utilizar E y L_z)

# Datos extra necesarios para la resolucion numerica

N=100 # Numero de iteraciones maximas, si llega a este numero, se asume que se ha ido muy lejos (o esta en una orbita estable)??????
h=0.01 # Tamaño del paso
