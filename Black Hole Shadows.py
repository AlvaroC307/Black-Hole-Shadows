# Importar Librerias utiles
import math
import random
import csv
from math import *

import Angle_to_Momentum
from Angle_to_Momentum import *
import Solving_Kerr_with_Christoffel
from Solving_Kerr_with_Christoffel import *


# Leer el fichero de inputs
csv_Input= open('./Input/Input.csv', 'r')
Reader_Input = csv.reader(csv_Input)

list_Input=[]
for row in Reader_Input:
    content_input = row[1]
    list_Input.append(content_input)


# Masa del agujero negro
M=eval(list_Input[0])

# Posicion del Observador y Condiciones Iniciales
t_0=eval(list_Input[1])
r_0=eval(list_Input[2])
phi_0=eval(list_Input[3])
theta_0= eval(list_Input[4])
coords_0=(t_0, r_0, phi_0, theta_0)

# Numero de Pixeles en un lado, el numero de pixeles total será, N_pix * N_pix
N_pix=eval(list_Input[5])

# Parametros del Agujero Negro (Spin, Carga electrica y Magnetica, etc)

a=eval(list_Input[6])
param=(M,a)

# Lo de arriba lo debe de dar el usuario, a partir de aqui, es el programa-----------------

rho2_Schwarzschild=r_0/2*M
angle_Schwarzschild=math.asin(math.sqrt((27*(rho2_Schwarzschild-1))/(4*(rho2_Schwarzschild**3)))) # Angulo de la sombra para un agujero negro de Schwarzschild con la misma masa
L_Schwarzschild=r_0*math.tan(angle_Schwarzschild) # Radio para el angulo de schwarzschild

L_screen=3*L_Schwarzschild # Multiplicamos por 4 para que haya espacio para verlo bien
paso=L_screen/N_pix


# Barra de Progreso
Porc_Avance=100/(N_pix+1)**2
k=0

# Definimos un fichero en el que escribir los resultados que nos interesen
file_In = open("./Data/Geodesics_In.csv", "w", newline="")
csv_In = csv.writer(file_In)
file_Out = open("./Data/Geodesics_Out.csv", "w", newline="")
csv_Out = csv.writer(file_Out)

for i in range(N_pix+1):
    for j in range(N_pix+1): 
            x=i*paso-L_screen/2
            y=j*paso-L_screen/2 # Estan mal definidas
            list_momentum=Screen_to_Momentum(x, y, *coords_0, *param)
            tupla_momentum=(list_momentum[0], list_momentum[1], list_momentum[2], list_momentum[3])
            In_or_out=Geodesic_Chris(*coords_0, *tupla_momentum , *param)

            print("Progreso:", int(k*Porc_Avance), "%")
            k+=1

            if In_or_out==1:
                csv_In.writerow([x, y])
                # Cae al agujero negro
            elif In_or_out==0:
                csv_Out.writerow([x, y])
                # No cae al agujero negro
            else:
                print('Error')

csv_Input.close()
# rnd=random.random()    Usar esto para cuando haga un montecarlo



