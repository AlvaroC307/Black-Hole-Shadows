# Importar Librerias utiles
import numpy as np
import math
import csv
# Importar otros ficheros de la carpeta

import Function_Metric
from Function_Metric import *
import Momento_Temporal_Inicial
from Momento_Temporal_Inicial import *
import Equations_to_Solve_Christoffel
from Equations_to_Solve_Christoffel import *

# Este codigo se tiene que ejecutar mucho, para cada resolucion de las ecuaciones

#Definicion del Hamitoniano 
def H(t, r, phi, theta, p_t, p_r, p_phi, p_theta):
     coord_H=(t,r,phi,theta)
     sumando_t_phi = p_t**2*Inv_G(0,0,*coord_H,*param)+p_phi**2*Inv_G(2,2,*coord_H,*param)+2*p_t*p_phi*Inv_G(0,2,*coord_H,*param)
     sumando_r_theta = p_r**2*Inv_G(1,1,*coord_H,*param)+p_theta**2*Inv_G(3,3,*coord_H,*param)
     return (sumando_t_phi+sumando_r_theta)/2

def Geodesic_Chris(t_0, r_0, phi_0, theta_0, p_t_0, p_r_0, p_phi_0, p_theta_0, M, a, N, h):

    # Parametros del Agujero Negro (Masa, Spin, Carga electrica y Magnetica, etc)
    param=(M, a)
    coords_0=(t_0, r_0, phi_0, theta_0)

    # Datos extra necesarios para la resolucion numerica
    # Numero de iteraciones maximas, si llega a este numero, se asume que se ha ido muy lejos (lo da el usuario o viene de base¿???????)
    N =1000
    h = 0.05  # Tamaño del paso (AHORA MISMO IGUAL PARA TODOS; SE PUEDE CAMBIAR) (Lo da el usuario o viene de base¿?¿?¿)

    # Los momentos son una-formas, es decir, indices bajados, pero las ecuaciones los utilizan como vectores
    #Calculo de los vectores p^mu iniciales como p^mu=sum(g^{mu nu}*p_nu)
    ps_t_0, ps_r_0, ps_phi_0, ps_theta_0 = 0, 0, 0, 0

    momento_sub_0=[p_t_0, p_r_0, p_phi_0, p_theta_0]
    for i in range(4):
        ps_t_0+=Inv_G(0, i, *coords_0, *param)*momento_sub_0[i]
        ps_r_0+=Inv_G(1, i, *coords_0, *param)*momento_sub_0[i]
        ps_phi_0+=Inv_G(2, i, *coords_0, *param)*momento_sub_0[i]
        ps_theta_0+=Inv_G(3, i, *coords_0, *param)*momento_sub_0[i]


    # Calculo de las Constantes del Movimiento para ciertas condiciones "iniciales"
    E = -p_t_0
    L_z = p_phi_0
    Q = (p_theta_0)**2-(a*E*math.cos(theta_0))**2+(L_z/math.tan(theta_0))**2
    # mu2 = 0  # Como son para geodesicas luminosas siempre se tomara mu^2=0, esto ya se ha tenido en cuenta en las
    # ecuaciones de hamilton siguientes, y los terminos proporcionales a mu no existen

    #-------------------------------------------------------------------------


    # Metodo de RK4 para 8 ecuaciones diferenciales de primer orden
    # Inicializar Vectores con las coordenadas y sus momentos, act hace referencia a los actuales y ant a los anteriores

    coord_act = [ps_t_0, ps_r_0, ps_phi_0, ps_theta_0, t_0, r_0, phi_0, theta_0]
    coord_ant = []
    Paso=[h,h,h,h,h,h,h,h] #En principio el paso es igual para las 8 ecuaciones

    veces_cambio_r=0
    veces_cambio_theta=0

    # Definimos un fichero en el que escribir los resultados que nos interesen
    file_manager = open("./Data/Prueba.csv", "w", newline="")
    csv_manager = csv.writer(file_manager)


    # Método RK4 como tal, empieza aqui-----------------------------------
    for i in range(N):

        # Las coordenadas actuales son las anteriores
        # 4 vectores 1x6, que simbolizan los valores de K_ij para el metodo RK4, en el siguiente orden: ps_mu---x_mu

        coord_ant = coord_act.copy()
        K1 = []
        K2 = []
        K3 = []
        K4 = []

        # Obtener los valores K_ij del metodo RK4
        for j in range(8):
            K1.append(Switch_punto(j, coord_ant[4], coord_ant[5], coord_ant[6], coord_ant[7], coord_ant[0], coord_ant[1], coord_ant[2], coord_ant[3]))
        for j in range(8):
            K2.append(Switch_punto(j, coord_ant[4]+(Paso[4]/2)*K1[4], coord_ant[5]+(Paso[5]/2)*K1[5], coord_ant[6]+(Paso[6]/2)*K1[6], coord_ant[7]+(Paso[7]/2)*K1[7],
            coord_ant[0]+(Paso[0]/2)*K1[0], coord_ant[1]+(Paso[1]/2)*K1[1], coord_ant[2]+(Paso[2]/2)*K1[2], coord_ant[3]+(Paso[3]/2)*K1[3]))
        for j in range(8):
            K3.append(Switch_punto(j, coord_ant[4]+(Paso[4]/2)*K2[4], coord_ant[5]+(Paso[5]/2)*K2[5], coord_ant[6]+(Paso[6]/2)*K2[6], coord_ant[7]+(Paso[7]/2)*K2[7],
            coord_ant[0]+(Paso[0]/2)*K2[0], coord_ant[1]+(Paso[1]/2)*K2[1], coord_ant[2]+(Paso[2]/2)*K2[2], coord_ant[3]+(Paso[3]/2)*K2[3]))
        for j in range(8):
            K4.append(Switch_punto(j, coord_ant[4]+(Paso[4])*K3[4], coord_ant[5]+(Paso[5])*K3[5], coord_ant[6]+(Paso[6])*K3[6], coord_ant[7]+(Paso[7])*K3[7],
            coord_ant[0]+(Paso[0])*K3[0], coord_ant[1]+(Paso[1])*K3[1], coord_ant[2]+(Paso[2])*K3[2], coord_ant[3]+(Paso[3])*K3[3]))

        # Obtener las coordenadas actuales
        for j in range(8):
            coord_act[j] = coord_ant[j]+(Paso[j]/6)*(K1[j]+2*K2[j]+2*K3[j]+K4[j])


        # Hacer que las constantes sigan siendo constantes, p^r y p^theta

        ps_r_cambio=Mom_Sup_r(coord_act[4], coord_act[5], coord_act[6], coord_act[7], coord_act[0], coord_act[1], coord_act[2], coord_act[3], *param)
        cambio_porc_r=abs(ps_r_cambio-coord_act[1])/abs(ps_r_cambio)

        if cambio_porc_r<0.01:
            coord_act[1]=ps_r_cambio
            veces_cambio_r+=1

        ps_theta_cambio=Mom_Sup_theta(coord_act[4], coord_act[5], coord_act[6], coord_act[7], coord_act[3], M, a, E, L_z, Q)
        cambio_porc_theta=abs(ps_theta_cambio-coord_act[3])/abs(ps_theta_cambio)

        if  cambio_porc_theta<0.01:
            coord_act[3]=ps_theta_cambio
            veces_cambio_theta+=1




        # Comprobaciones si se va al horizonte de eventos o no (de momento lo voy a comprobar con el horizonte de eventros teorico)
        # Cuando haya que hacer el programa de verdad bien, cambiarlo
        R_horizon=M+math.sqrt(M**2-a**2)
        if coord_act[5]<=R_horizon:
            # Apuntar en un fichero si es black hole o no
            file_manager.close()
            return 0 # Esto para la funcion


        # Escribir en un fichero

        csv_manager.writerow(
            coord_act)

        # Lo que queda del for es simplemente para comprobar cosas
        
        #p_t, p_r, p_phi, p_theta = 0, 0, 0, 0
        #coords_tupla_act=(coord_act[4],coord_act[5],coord_act[6],coord_act[7])  
        #for i in range(4):
        #    p_t+=G(0, i, *coords_tupla_act, *param)*coord_act[i]
        #    p_r+=G(1, i, *coords_tupla_act, *param)*coord_act[i]
        #    p_phi+=G(2, i, *coords_tupla_act, *param)*coord_act[i]
        #    p_theta+=G(3, i, *coords_tupla_act, *param)*coord_act[i]

        #print(coord_act[3]**2+(cos(coord_act[7]))**2*(-(a*coord_act[0])**2+(coord_act[2]/(sin(coord_act[7])))**2))
        #print(H(coord_act[4], coord_act[5], coord_act[6], coord_act[7], p_t, p_r, p_phi, p_theta))
        #print(-p_t)
        #print(p_phi)
        #print(coord_ant[1]-coord_act[1])



    # Apuntar que no es sombra en un fichero
    file_manager.close()
    return 0


# Para hacer pruebas:
M=1
a=0
r_0 = 5*M
theta_0 = math.pi/4
phi_0 = 0
t_0 = 0
p_r_0 = 1.0
p_theta_0 = 0.0
p_phi_0 = 0.0