# Importar Librerias utiles
import numpy as np
import sympy as sp
import math
import csv
# Importar otros ficheros de la carpeta

import Metric
from Metric import *

# Este codigo se tiene que ejecutar mucho, para cada resolucion de las ecuaciones

# Parametros del Agujero Negro (Masa, Spin, Carga electrica y Magnetica, etc)
M = 1
a = 0
# Condiciones "Iniciales" (finales) del foton al llegar a la pantalla
# Los momentos son una-formas, es decir, indices bajados
r_0 = 5*M
theta_0 = math.pi/4
phi_0 = 0
t_0 = 0
p_t_0 = 1
p_r_0 = -1.0
p_theta_0 = 0.0
p_phi_0 = 0.0

# Calculo de las Constantes del Movimiento para ciertas condiciones "iniciales"
E = -p_t_0
L_z = p_phi_0
Q = (p_theta_0)**2-(a*E*math.cos(theta_0))**2+(L_z/math.tan(theta_0))**2
mu2 = 0  # Como son para geodesicas luminosas siempre se tomara mu^2=0, esto ya se ha tenido en cuenta en las
# ecuaciones de hamilton siguientes, y los terminos proporcionales a mu no existen


# Definicion de Delta y rho^2

def Delta(r):
    return r**2+a**2-2*M*r


def rho2(r, theta):
    return r**2+(a*math.cos(theta))**2


# Definicion del Hamitoniano

# def H(r, theta, p_r, p_theta):
#     sumando1 = (a*L_z-(r**2+a**2)*E)**2/(Delta(r))
#     sumando2 = (L_z-a*E*(math.sin(theta))**2)**2/(math.sin(theta))**2
#     return (Delta(r)*p_r**2+p_theta**2+sumando1+sumando2)/(2*rho2(r, theta))


def H(r,theta,p_r,p_theta):
    return 0

# Definir las 6 funciones que se van a integrar

def r_punto(r, theta, p_r):
    return ((Delta(r)*p_r)/rho2(r, theta))


def theta_punto(r, theta, p_theta):
    return (p_theta/rho2(r, theta))


def p_r_punto(r, theta, p_r, p_theta):
    sumando1 = (-a*E*(L_z-a*E*(math.sin(theta))**2))/(math.sin(theta))**2
    sumando2 = ((L_z-a*E*(math.sin(theta))**2)**2)/(math.sin(theta))**4
    return (-math.sin(2*theta)/rho2(r, theta))*(H(r, theta, p_r, p_theta)+sumando1-sumando2)


def p_theta_punto(r, theta, p_r, p_theta):
    sumando1 = (-2*r*E)*(a*L_z-(r**2+a**2)*E)/Delta(r)
    sumando2 = (-2*(r-M)*(a*L_z-(r**2+a**2)*E)**2)/(Delta(r))**2
    return (2*r*H(r, theta, p_r, p_theta))/(rho2(r, theta))-((r-M)*p_r**2-sumando1+sumando2)/(rho2(r, theta))


def t_punto(r, theta):
    return ((Delta(r)*rho2(r, theta)+2*M*r*(r**2+a**2))/(Delta(r)*rho2(r, theta)))*E-(2*M*r*a/(Delta(r)*rho2(r, theta)))*L_z


def phi_punto(r, theta):
    return ((2*M*r*a)/(Delta(r)*rho2(r, theta)))*E+((rho2(r, theta)-2*M*r)/(Delta(r)*rho2(r, theta)*(math.sin(theta))**2))*L_z


# ESTA FUNCION IGUAL ES UN LIO Y NO HACE FALTA, PREGUNTAR A MARIO

def Switch_punto(i, r, theta, p_r, p_theta):
    if i == 0:
        return r_punto(r, theta, p_r)
    elif i == 1:
        return theta_punto(r, theta, p_theta)
    elif i == 2:
        return p_r_punto(r, theta, p_r, p_theta)
    elif i == 3:
        return p_theta_punto(r, theta, p_r, p_theta)
    elif i == 4:
        return t_punto(r, theta)
    elif i == 5:
        return phi_punto(r, theta)

# Metodo de RK4 para 6 ecuaciones diferenciales de primer orden (p_t y p_phi están ya calculadas al utilizar E y L_z)

# Datos extra necesarios para la resolucion numerica


# Numero de iteraciones maximas, si llega a este numero, se asume que se ha ido muy lejos (o esta en una orbita estable)??????
N = 5000
h = 0.01  # Tamaño del paso


# Inicializar 6 Vectores 1x2, donde el elemento 0 son los valores i, mientras que el elemento 1 son los valores i+1


coord_act = [r_0, theta_0, p_r_0, p_theta_0, t_0, phi_0]
coord_ant = []

# 4 vectores 1x6, que simbolizan los valores de K_ij para el metodo RK4, en el siguiente orden: r-theta-p_r-p_theta-t-phi

file_manager = open("./Data/Prueba.csv", "w", newline="")
csv_manager = csv.writer(file_manager)

for i in range(N):

    # Las coordenadas actuales son las anteriores

    coord_ant = coord_act.copy()
    K1 = []
    K2 = []
    K3 = []
    K4 = []

    # Obtener los valores K_ij del metodo RK4
    for j in range(6):
        K1.append(Switch_punto(
            j, coord_ant[0], coord_ant[1], coord_ant[2], coord_ant[3]))
    for j in range(6):
        K2.append(Switch_punto(j, coord_ant[0]+(h/2)*K1[0], coord_ant[1]+(
            h/2)*K1[1], coord_ant[2]+(h/2)*K1[2], coord_ant[3]+(h/2)*K1[3]))
    for j in range(6):
        K3.append(Switch_punto(j, coord_ant[0]+(h/2)*K2[0], coord_ant[1]+(
            h/2)*K2[1], coord_ant[2]+(h/2)*K2[2], coord_ant[3]+(h/2)*K2[3]))
    for j in range(6):
        K4.append(Switch_punto(
            j, coord_ant[0]+h*K3[0], coord_ant[1]+h*K3[1], coord_ant[2]+h*K3[2], coord_ant[3]+h*K3[3]))

    # Obtener las coordenadas actuales
    for j in range(6):
        coord_act[j] = coord_ant[j]+(h/6)*(K1[j]+2*K2[j]+2*K3[j]+K4[j])

    # Escribir en un fichero

    csv_manager.writerow(
        coord_act)


file_manager.close()
print("ta chido")
