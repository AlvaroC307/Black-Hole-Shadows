# Importar Librerias utiles
import math
import csv
import numpy as np
import time

# Importar otros ficheros de la carpeta
from Function_Metric import Inv_G
import Momento_Temporal_Inicial as mti
from Equations_to_Solve_Christoffel import Switch_punto
from Angle_to_Momentum import Screen_to_Momentum_Forwards
import Representation_Geodesic as Repr_Geo
from Initial_Values import M, t_0_Geo, r_0_Geo, phi_0_Geo, theta_0_Geo, precision_Geo, r_limit_Geo, constantes
from Initial_Values import p_r_0_Geo, p_phi_0_Geo, p_theta_0_Geo, i_Geo, j_Geo, Momentum_or_Screen, N_pix, Factor_Screen
# Este codigo se tiene que ejecutar mucho, para cada resolucion de las ecuaciones

# Definición paso adaptativo como función que cambie el paso en función de la distancia a r=0
def Paso_adap_precision(r:float, theta:float)->int|float: # Es más detallado que el que se usa en Solving_Kerr_with_Christoffel.py

    if (r<3*M):
        h=0.01
    elif (r<6*M):
        h=0.05
    elif (r<10*M):
        h=0.1
    elif (r<15*M):
        h=0.5
    elif (r<20*M):
        h=1 
    elif (r<50*M): 
        h=5 
    else:
        h=10

    # Para evitar problemas al tener metricas con singularidades en sin(theta)=0, cuando se acerca a 0 o pi
    # el paso se vuelve mucho más lento
    if (abs(math.sin(theta))<0.09): 
        h=0.01 
    return (precision_Geo*h*M)


def Geodesic(p_t_0:float, p_r_0:float, p_phi_0:float, p_theta_0:float)->str:

    # Escribir los parámetros y coordenadas iniciales del problema en dos tuplas
    coords_0=(t_0_Geo, r_0_Geo, phi_0_Geo, theta_0_Geo)

    tau=0 #Definimos el tiempo propio (o lambda para geodesicas luminosas) como tau=0 cuando se comienza el programa

    #---------------------------Datos extra necesarios para la resolucion numerica
    N =5000000 # Numero de iteraciones maximas, si llega a este numero, se asume que está en órbita
    Dif_t_Horizon=60*precision_Geo # Parámetro que mide si cambia demasiado la coord radial y ha caido al Agujero Negro
    Dif_r_Horizon=60*precision_Geo # Parámetro que mide si cambia demasiado la coord temporal y ha caido al Agujero Negro
    #----------------------------------------

    # Los momentos son una-formas, es decir, indices bajados, pero las ecuaciones los utilizan como vectores 
    #Calculo de los vectores p^mu iniciales como p^mu=sum(g^{mu nu}*p_nu)
    ps_t_0, ps_r_0, ps_phi_0, ps_theta_0 = 0, 0, 0, 0 #IMPORTANTE: (ps_x=p^x)

    momento_sub_0=np.array([p_t_0, p_r_0, p_phi_0, p_theta_0]) # Lista de los momentos iniciales con SUBindices
    for i in range(4):
        ps_t_0+=Inv_G(0, i, *coords_0)*momento_sub_0[i]
        ps_r_0+=Inv_G(1, i, *coords_0)*momento_sub_0[i]
        ps_phi_0+=Inv_G(2, i, *coords_0)*momento_sub_0[i]
        ps_theta_0+=Inv_G(3, i, *coords_0)*momento_sub_0[i]

    print(ps_t_0)

    # Calculo de las Constantes del Movimiento para ciertas condiciones "iniciales"
    E = -p_t_0
    L_z = p_phi_0
    C = (p_theta_0)**2-(constantes['a']*E*math.cos(theta_0_Geo))**2+(L_z/math.tan(theta_0_Geo))**2

    # Metodo de RK4 para 8 ecuaciones diferenciales de primer orden
    # Inicializar Vectores con las coordenadas y sus momentos.
    # IMPORTANTE: coord_act hace referencia a los actuales y coord_ant a los anteriores

    coord_act = np.array([ps_t_0, ps_r_0, ps_phi_0, ps_theta_0, t_0_Geo, r_0_Geo, phi_0_Geo, theta_0_Geo])
    

    # Definimos un fichero en el que escribir los resultados que nos interesen comprobar en caso de problema con cierta geodesica
    file_geodesic = open("./Data/Specific_Geodesic.csv", "w", newline="")
    csv_geodesic = csv.writer(file_geodesic)


    # Método RK4 como tal, empieza aqui------------------------------------------------------
    for i in range(N):

        coord_ant = coord_act.copy() # Se copian las coordenadas actuales a las anteriores para comenzar

        # Inicializamos 4 listas 1x8, que simbolizan los valores de K_ij para el metodo RK4, en el siguiente orden: [ps_mu,x_mu] 
        # Donde el indice mu va en el orden (t,r,phi,theta)
        K1 = np.empty(8)
        K2 = np.empty(8)
        K3 = np.empty(8)
        K4 = np.empty(8)

        h=Paso_adap_precision(coord_ant[5], coord_ant[7]) # Se encuentra el paso para cada iteración

        # Obtener los valores K_ij del metodo RK4
        # IMPORTANTE EL SIGNO NEGATIVO ES POR QUÉ LAS ECUACIONES ESTÁN ESCRITAS CON UN MENOS PARA HACER BACKWARDS RAY-TRACING
        for j in range(8):
            K1[j]=-Switch_punto(j, coord_ant[0], coord_ant[1], coord_ant[2], coord_ant[3],
            (coord_ant[4], coord_ant[5], coord_ant[6], coord_ant[7]))
        coord_ant_for_K2=coord_ant+((h/2)*K1)

        for j in range(8):
            K2[j]=-Switch_punto(j, coord_ant_for_K2[0], coord_ant_for_K2[1], coord_ant_for_K2[2], coord_ant_for_K2[3], 
            (coord_ant_for_K2[4], coord_ant_for_K2[5], coord_ant_for_K2[6], coord_ant_for_K2[7]))
        coord_ant_for_K3=coord_ant+((h/2)*K2)

        for j in range(8):
            K3[j]=-Switch_punto(j, coord_ant_for_K3[0], coord_ant_for_K3[1], coord_ant_for_K3[2], coord_ant_for_K3[3], 
            (coord_ant_for_K3[4], coord_ant_for_K3[5], coord_ant_for_K3[6], coord_ant_for_K3[7]))
        coord_ant_for_K4=coord_ant+(h*K3)

        for j in range(8):
            K4[j]=-Switch_punto(j, coord_ant_for_K4[0], coord_ant_for_K4[1], coord_ant_for_K4[2], coord_ant_for_K4[3],
            (coord_ant_for_K4[4], coord_ant_for_K4[5], coord_ant_for_K4[6], coord_ant_for_K4[7]))

        # Obtener las coordenadas actuales gracias a los valores K_ij
        coord_act = coord_ant+(h/6)*(K1+2*K2+2*K3+K4)

        # Obtener el tiempo propio.

        tau=tau+h

        #-----------------------Comprobaciones para parar el programa

        # La partícula cae al horizonte de eventos (que el tiempo cambie mucho)
        if (abs(coord_act[4]-coord_ant[4])>=Dif_t_Horizon) or (abs(coord_act[5]-coord_ant[5])>=Dif_r_Horizon):
            return "fallen inside the Black Hole" # Esto significa que cae al agujero negro

        # La partícula se va al infinito y el agujero negro es despreciable
        # (Si la coordenada radial es mayor que r_limit y sigue aumentando)
        if ((coord_act[5])>=r_limit_Geo) and ((coord_act[5]-coord_ant[5])>0): 
            return "gone to Infinity" # Esto significa que se va al infinito


        # Escribir en un fichero las coordenadas y el tiempo propio de la geodesica
        csv_geodesic.writerow([coord_act[4], coord_act[5], coord_act[6], coord_act[7], tau])


    file_geodesic.close() # Cerrar el fichero 

    return "stayed in pseudo-circular orbit" # Esto significa que no cae al agujero negro en N pasos pero tampoco se va a infinito, por lo que asumimos que orbita 



def main():

    time_Computing_initial=time.time()

    if Momentum_or_Screen == "Momentum":
        # Encontramos la componente temporal del momento inicial que cumpla p^2=m^2
        p_t_0_Geo=mti.Mom_temp_massive(t_0_Geo, r_0_Geo, phi_0_Geo, theta_0_Geo, p_r_0_Geo, p_phi_0_Geo, p_theta_0_Geo)
        tuple_momentum = (p_t_0_Geo, p_r_0_Geo, p_phi_0_Geo, p_theta_0_Geo)

    elif Momentum_or_Screen == "Screen":

        # Radio de la sombra del agujero negro de Schwarzschild equivalente
        L_screen = 3*math.sqrt(3)*M*Factor_Screen

        list_points_x = np.linspace(-L_screen/2 + (L_screen/(2*N_pix)), L_screen/2 - (L_screen/(2*N_pix)), N_pix)
        list_points_y = np.linspace(L_screen/2 - (L_screen/(2*N_pix)), -L_screen/2 + (L_screen/(2*N_pix)), N_pix)
        x_Geo=list_points_x[i_Geo]
        y_Geo=list_points_y[j_Geo]
        tuple_momentum = Screen_to_Momentum_Forwards(x_Geo, y_Geo) # Encontramos el cuatrimomento asociado con un punto de la pantalla dado

    trayectory = Geodesic(*tuple_momentum) # Calculamos la geodésica

    print(f"The particle has {trayectory}.") # Nos dice que esta en orbita, ha caido al agujero negro o se ha ido al infinito
    print(f"The program has run for {time.time()-time_Computing_initial} seconds.")

    # Generamos las graficas que nos interesan
    Repr_Geo.plot_tr() 
    Repr_Geo.plot_taur()
    Repr_Geo.Polar_plot()
    
if __name__ == '__main__': #Llamar al main()
    main()
