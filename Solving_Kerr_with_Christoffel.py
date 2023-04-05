# Importar Librerias utiles
import math
import csv
import numpy as np

# Importar otros ficheros de la carpeta
from Function_Metric import Inv_G
import Momento_Temporal_Inicial as mti
from Equations_to_Solve_Christoffel import Switch_punto
import Background as Backg
from Initial_Values import M, t_0, r_0, phi_0, theta_0, Back_Im, constantes, r_limit
# Este codigo se tiene que ejecutar mucho, para cada resolucion de las ecuaciones

# Definición paso adaptativo como función que cambie el paso en función de la distancia a r=0
def Paso_adap(r:float, theta:float)->int|float:
    

    if (r<7*M):
        h=0.1
    elif (r<10*M):
        h=0.4
    elif (r<20*M):
        h=2
    elif (r<60*M):
        h=5
    else:
        h=10

    """ 
    if (r>60*M):
        h=10
    elif (r>20*M):
        h=6 # Antes era 5
    elif (r>10*M):
        h=3 # Antes era 2.5
    else:
        h=0.1 """

    # Para evitar problemas al tener metricas con singularidades en sin(theta)=0, cuando se acerca a 0 o pi
    # el paso se vuelve mucho más lento
    if ((abs(theta))<0.05) or ((abs(theta-math.pi))<0.05):
        h=0.01 # Antes era 0.01
    return h



def Geodesic_Chris(p_t_0:float, p_r_0:float, p_phi_0:float, p_theta_0:float)->str|list:

    # Escribir los parámetros y coordenadas iniciales del problema en dos tuplas
    coords_0=(t_0, r_0, phi_0, theta_0)

    # Datos extra necesarios para la resolucion numerica
    N =5000 # Numero de iteraciones maximas, si llega a este numero, se asume que se ha ido muy lejos
    Dif_t_Horizon=15 # Parámetro que mide si cambia demasiado la coord radial y ha caido al Agujero Negro
    Dif_r_Horizon=30 # Parámetro que mide si cambia demasiado la coord temporal y ha caido al Agujero Negro

    # Los momentos son una-formas, es decir, indices bajados, pero las ecuaciones los utilizan como vectores 
    #Calculo de los vectores p^mu iniciales como p^mu=sum(g^{mu nu}*p_nu)
    ps_t_0, ps_r_0, ps_phi_0, ps_theta_0 = 0, 0, 0, 0 #IMPORTANTE: (ps_x=p^x)

    momento_sub_0=np.array([p_t_0, p_r_0, p_phi_0, p_theta_0]) # Lista de los momentos iniciales con SUBindices
    for i in range(4):
        ps_t_0+=Inv_G(0, i, *coords_0)*momento_sub_0[i]
        ps_r_0+=Inv_G(1, i, *coords_0)*momento_sub_0[i]
        ps_phi_0+=Inv_G(2, i, *coords_0)*momento_sub_0[i]
        ps_theta_0+=Inv_G(3, i, *coords_0)*momento_sub_0[i]


    # Calculo de las Constantes del Movimiento para ciertas condiciones "iniciales"
    E = -p_t_0
    L_z = p_phi_0
    C = (p_theta_0)**2-(constantes['a']*E*math.cos(theta_0))**2+(L_z/math.tan(theta_0))**2

    #-------------------------------------------------------------------------


    # Metodo de RK4 para 8 ecuaciones diferenciales de primer orden
    # Inicializar Vectores con las coordenadas y sus momentos.
    # IMPORTANTE: coord_act hace referencia a los actuales y coord_ant a los anteriores

    coord_act = np.array([ps_t_0, ps_r_0, ps_phi_0, ps_theta_0, t_0, r_0, phi_0, theta_0])
    

    # Definimos un fichero en el que escribir los resultados que nos interesen comprobar en caso de problema con cierta geodesica
    """ file_manager = open("./Data/Prueba.csv", "w", newline="")
    csv_manager = csv.writer(file_manager) """


    # Método RK4 como tal, empieza aqui------------------------------------------------------
    for i in range(N):

        coord_ant = coord_act.copy() # Se copian las coordenadas actuales a las anteriores para comenzar

        # 4 listas 1x8, que simbolizan los valores de K_ij para el metodo RK4, en el siguiente orden: ps_mu---x_mu
        # Donde el eje mu va en el orden t-r-phi-theta
        K1 = np.empty(8)
        K2 = np.empty(8)
        K3 = np.empty(8)
        K4 = np.empty(8)

        h=Paso_adap(coord_ant[5], coord_ant[7]) # Se elige el paso para cada iteracion

        # Obtener los valores K_ij del metodo RK4
        for j in range(8):
            K1[j]=Switch_punto(j, coord_ant[0], coord_ant[1], coord_ant[2], coord_ant[3],
            (coord_ant[4], coord_ant[5], coord_ant[6], coord_ant[7]))
        coord_ant_for_K2=coord_ant+((h/2)*K1)

        for j in range(8):
            K2[j]=Switch_punto(j, coord_ant_for_K2[0], coord_ant_for_K2[1], coord_ant_for_K2[2], coord_ant_for_K2[3], 
            (coord_ant_for_K2[4], coord_ant_for_K2[5], coord_ant_for_K2[6], coord_ant_for_K2[7]))
        coord_ant_for_K3=coord_ant+((h/2)*K2)

        for j in range(8):
            K3[j]=Switch_punto(j, coord_ant_for_K3[0], coord_ant_for_K3[1], coord_ant_for_K3[2], coord_ant_for_K3[3], 
            (coord_ant_for_K3[4], coord_ant_for_K3[5], coord_ant_for_K3[6], coord_ant_for_K3[7]))
        coord_ant_for_K4=coord_ant+(h*K3)

        for j in range(8):
            K4[j]=Switch_punto(j, coord_ant_for_K4[0], coord_ant_for_K4[1], coord_ant_for_K4[2], coord_ant_for_K4[3],
            (coord_ant_for_K4[4], coord_ant_for_K4[5], coord_ant_for_K4[6], coord_ant_for_K4[7]))

        # Obtener las coordenadas actuales gracias a los valores K_ij
        coord_act = coord_ant+(h/6)*(K1+2*K2+2*K3+K4)


        # Hacer que las constantes sigan siendo constantes, p^r y p^theta----------------------

        ps_r_cambio=mti.Mom_Sup_r(coord_act[0], coord_act[1], coord_act[2], coord_act[3], (coord_act[4], coord_act[5], coord_act[6], coord_act[7]))
        if ps_r_cambio=="Imaginary":
            ps_r_cambio="Imaginary"# Esto es estupido hay que quitarlo
        #   return "Black" # Esto significa que cae al agujero negro (COMPROBAR VERACIDAD DEL CLAIM)(QUIZÁ HASTA SEA IMPOSIBLE)
        else:
            cambio_porc_r=abs(ps_r_cambio-coord_act[1])/abs(coord_act[1])
            if cambio_porc_r<0.01:
                coord_act[1]=ps_r_cambio
        

        #ps_theta_cambio=mti.Mom_Sup_theta(coord_act[4], coord_act[5], coord_act[6], coord_act[7], coord_act[3], M, a, E, L_z, C)
        #cambio_porc_theta=abs(ps_theta_cambio-coord_act[3])/abs(coord_act[3])

        #if  cambio_porc_theta<0.01:
        #    coord_act[3]=ps_theta_cambio
        #    veces_cambio_theta+=1

        # Fin del hacer que las constantes del movimiento sigan cte--------------------------------------------


        # Escribir en un fichero los momentos y coordenadas para comprobar un geodesica especifica
        #csv_manager.writerow(coord_act)


        # Comprobaciones si se va al horizonte de eventos o no (que el tiempo cambie mucho o que la coordenada radial cambie demasiado)
        if (abs(coord_act[4]-coord_ant[4])>=Dif_t_Horizon) or abs(coord_act[5]-coord_ant[5])>=Dif_r_Horizon:
            return "Black" # Esto significa que cae al agujero negro


        #Si la coordenada radial es mayor que r_limit y aumentando se considera que se va al infinito y no cae al Agujero Negro
        if ((coord_act[5])>=r_limit) and ((coord_act[5]-coord_ant[5])>0): 
            # Elegir el color en el que acaba al llegar a r_limit
            if Back_Im=="C":
                Back_Colour=Backg.Sphere_Quadrants(coord_act[5], coord_act[6], coord_act[7]) 
            elif Back_Im=="I":
                Back_Colour=Backg.Background_Image(coord_act[5], coord_act[6], coord_act[7])
            return Back_Colour # Esto significa que se va al infinito


    #file_manager.close() # Cerrar el fichero para comprobar geodesicas aisladas

    return "Pink" # Esto significa que no cae al agujero negro en N pasos pero tampoco se va a infinito


# Para hacer pruebas de geodesicas especificas:--------------------------------------------------------
"""
from Angle_to_Momentum import * # Este solo es util para realizar las pruebas al final en caso de error y querer ver una unica geodesica
M=1
a=0.9
t_0=0
r_0 = 100*M
theta_0 = math.pi/2
phi_0 = math.pi/2
coords_0=(t_0, r_0, phi_0, theta_0)
param=(M, a)

#Pruebas con el momento puesto con las coordenadas x, y--------------

x,y=0.07726121118594291,5.331023571830061

list_momentum = Screen_to_Momentum(x, y, *coords_0, *param)
tupla_momentum = (list_momentum[0], list_momentum[1], list_momentum[2], list_momentum[3])
Pixel_Color = Geodesic_Chris("C", 50, *coords_0, *tupla_momentum, *param)
print(Pixel_Color) 
 """
# Puebas con el momento puesto a mano---------------

""" p_r_0 = 1
p_theta_0 = 0
p_phi_0 = 0
p_t_0=mti.Mom_temp(t_0,r_0,phi_0,theta_0,p_r_0,p_phi_0,p_theta_0)
Geodesic_Chris(p_t_0, p_r_0, p_phi_0, p_theta_0) """
