# Importar Librerias utiles
import numpy as np
import math
import csv
#import time
# Importar otros ficheros de la carpeta


from Function_Metric import *
import Momento_Temporal_Inicial
from Momento_Temporal_Inicial import *
from Equations_to_Solve_Christoffel import *
import Background as Backg
from Angle_to_Momentum import *

# Este codigo se tiene que ejecutar mucho, para cada resolucion de las ecuaciones

#Definicion del Hamitoniano 
def H(t, r, phi, theta, p_t, p_r, p_phi, p_theta, M, a):
     coord_H=(t,r,phi,theta)
     param=(M, a)
     sumando_t_phi = p_t**2*Inv_G(0,0,*coord_H,*param)+p_phi**2*Inv_G(2,2,*coord_H,*param)+2*p_t*p_phi*Inv_G(0,2,*coord_H,*param)
     sumando_r_theta = p_r**2*Inv_G(1,1,*coord_H,*param)+p_theta**2*Inv_G(3,3,*coord_H,*param)
     return (sumando_t_phi+sumando_r_theta)/2


# Definición paso adaptativo como función que cambie el paso en función de la distancia a r=0
def Paso_adap(r, theta, M):
    if (r>60*M):
        h=5
    elif (r>20*M):
        h=2
    elif (r>10*M):
        h=1
    elif (r>4*M):
        h=0.1
    else:
        h=0.05

    if (abs(theta))<0.05:
        h=0.01
    return h

def Geodesic_Chris(t_0, r_0, phi_0, theta_0, p_t_0, p_r_0, p_phi_0, p_theta_0, M, a):
    #Time_program_initial=time.time()
    # Parametros del Agujero Negro (Masa, Spin, Carga electrica y Magnetica, etc)
    param=(M, a)
    coords_0=(t_0, r_0, phi_0, theta_0)
    # Datos extra necesarios para la resolucion numerica
    # Numero de iteraciones maximas, si llega a este numero, se asume que se ha ido muy lejos 
    N =5000
    r_limit=10*M # Parámetro para a partir de que radio se considera que la métrica a degenerado a Minkowski

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

        h=Paso_adap(coord_act[5], coord_act[7] ,M)

        Paso=[h,h,h,h,h,h,h,h]

        # Obtener los valores K_ij del metodo RK4
        for j in range(8):
            K1.append(Switch_punto(j, coord_ant[4], coord_ant[5], coord_ant[6], coord_ant[7], coord_ant[0], coord_ant[1], coord_ant[2], coord_ant[3], *param))
        for j in range(8):
            K2.append(Switch_punto(j, coord_ant[4]+(Paso[4]/2)*K1[4], coord_ant[5]+(Paso[5]/2)*K1[5], coord_ant[6]+(Paso[6]/2)*K1[6], coord_ant[7]+(Paso[7]/2)*K1[7],
            coord_ant[0]+(Paso[0]/2)*K1[0], coord_ant[1]+(Paso[1]/2)*K1[1], coord_ant[2]+(Paso[2]/2)*K1[2], coord_ant[3]+(Paso[3]/2)*K1[3], *param))
        for j in range(8):
            K3.append(Switch_punto(j, coord_ant[4]+(Paso[4]/2)*K2[4], coord_ant[5]+(Paso[5]/2)*K2[5], coord_ant[6]+(Paso[6]/2)*K2[6], coord_ant[7]+(Paso[7]/2)*K2[7],
            coord_ant[0]+(Paso[0]/2)*K2[0], coord_ant[1]+(Paso[1]/2)*K2[1], coord_ant[2]+(Paso[2]/2)*K2[2], coord_ant[3]+(Paso[3]/2)*K2[3], *param))
        for j in range(8):
            K4.append(Switch_punto(j, coord_ant[4]+(Paso[4])*K3[4], coord_ant[5]+(Paso[5])*K3[5], coord_ant[6]+(Paso[6])*K3[6], coord_ant[7]+(Paso[7])*K3[7],
            coord_ant[0]+(Paso[0])*K3[0], coord_ant[1]+(Paso[1])*K3[1], coord_ant[2]+(Paso[2])*K3[2], coord_ant[3]+(Paso[3])*K3[3], *param))

        # Obtener las coordenadas actuales
        for j in range(8):
            coord_act[j] = coord_ant[j]+(Paso[j]/6)*(K1[j]+2*K2[j]+2*K3[j]+K4[j])


        # Hacer que las constantes sigan siendo constantes, p^r y p^theta----------------------

        ps_r_cambio=Mom_Sup_r(coord_act[4], coord_act[5], coord_act[6], coord_act[7], coord_act[0], coord_act[1], coord_act[2], coord_act[3], *param)
        if ps_r_cambio=="Imaginary":
            print("Imaginario")
        #    return "Black" # Esto significa que cae al agujero negro (COMPROBAR VERACIDAD DEL CLAIM)(QUIZÁ HASTA SEA IMPOSIBLE)
        else:
            cambio_porc_r=abs(ps_r_cambio-coord_act[1])/abs(coord_act[1])
            if cambio_porc_r<0.01:
                coord_act[1]=ps_r_cambio
                #veces_cambio_r+=1
                #print(veces_cambio_r)
        

        #ps_theta_cambio=Mom_Sup_theta(coord_act[4], coord_act[5], coord_act[6], coord_act[7], coord_act[3], M, a, E, L_z, Q)
        #cambio_porc_theta=abs(ps_theta_cambio-coord_act[3])/abs(coord_act[3])

        #if  cambio_porc_theta<0.01:
        #    coord_act[3]=ps_theta_cambio
        #    veces_cambio_theta+=1

        # Fin del hacer que las cte sigan cte----------------------------------


        # Escribir en un fichero
        csv_manager.writerow(coord_act)


        # Comprobaciones si se va al horizonte de eventos o no (que el tiempo cambie mucho)
        if (abs(coord_act[4]-coord_ant[4])>=10) or abs(coord_act[5]-coord_ant[5])>=20:
        #if (G(1, 1, coord_act[4], coord_act[5], coord_act[6], coord_act[7], *param)<=0):
        #    Time_program_final=time.time()
        #    print(Time_program_final-Time_program_initial)
            return "Black" # Esto significa que cae al agujero negro

        
        if ((coord_act[5])>=r_limit) and ((coord_act[5]-coord_ant[5])>0): #Elijo un valor más pequeño que 10?
        #    Time_program_final=time.time()
        #    print(Time_program_final-Time_program_initial)
            Back_Colour=Backg.Sphere_Quadrants(coord_act[5], coord_act[6], coord_act[7])
            return Back_Colour # Esto significa que se va al infinito




       

    file_manager.close()

    #Back_Colour=Backg.Sphere_Quadrants(coord_act[5], coord_act[6], coord_act[7])
    return "White" #Back_Colour # Esto significa que no cae al agujero negro en N pasos


# Para hacer pruebas:
""" M=1
a=0.9
t_0=0
r_0 = 100*M
theta_0 = math.pi/2
phi_0 = math.pi/2
coords_0=(t_0, r_0, phi_0, theta_0)
param=(M, a)

#Pruebas con el momento puesto con las coordenadas x, y

x,y=0.07726121118594291,-5.176501149458176

list_momentum = Screen_to_Momentum(x, y, *coords_0, *param)
tupla_momentum = (list_momentum[0], list_momentum[1], list_momentum[2], list_momentum[3])
Pixel_Color = Geodesic_Chris(*coords_0, *tupla_momentum, *param)
print(Pixel_Color) """

# Puebas con el momento puesto a mano

#p_r_0 = 1
#p_theta_0 = 0
#p_phi_0 = 0
#p_t_0=Mom_temp(t_0,r_0,phi_0,theta_0,p_r_0,p_phi_0,p_theta_0,M,a)
#Geodesic_Chris(t_0, r_0, phi_0, theta_0, p_t_0, p_r_0, p_phi_0, p_theta_0, M, a)
