# Importar Librerias utiles
import math
import time
import csv
from math import *

from concurrent.futures import *

import Angle_to_Momentum
from Angle_to_Momentum import *
import Solving_Kerr_with_Christoffel
from Solving_Kerr_with_Christoffel import *


def Screen(r_0, M): # Calculo del tamaño de la pantalla
    rho2_Schwarzschild=r_0/2*M
    angle_Schwarzschild=math.asin(math.sqrt((27*(rho2_Schwarzschild-1))/(4*(rho2_Schwarzschild**3)))) # Angulo de la sombra para un agujero negro de Schwarzschild con la misma masa
    L_Schwarzschild=r_0*math.tan(angle_Schwarzschild) # Radio para el angulo de schwarzschild

    L_screen=3*L_Schwarzschild # Multiplicamos por 4 para que haya espacio para verlo bien
    return L_screen





def Black_Hole_Geodesic(x0, x1, y0, y1, N_pix_little, list_Input): 


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

    if (N_pix%2)==1: # Para que N_pix sea par y se pueda divir facil en 4 cuadrantes
        N_pix+=1

    # Parametros del Agujero Negro (Spin, Carga electrica y Magnetica, etc)

    a=eval(list_Input[6])
    param=(M,a)

    # Barra de Progreso
    Porc_Avance=100/(N_pix)**2


    All_data_Quadrant=[]
    Lx=x1-x0
    Ly=y1-y0         
    paso_x=Lx/N_pix_little
    paso_y=Ly/N_pix_little

    x0=x0+paso_x/2
    y0=y0+paso_y/2 # Esto es para que luego se pongan en el centro del pixel y no en una esquina

    k=0
    for i in range(N_pix_little):
        One_line_data_quadrant=[]

        for j in range(N_pix_little): 
                x=x0+j*paso_x
                y=y0+i*paso_y 
                list_momentum=Screen_to_Momentum(x, y, *coords_0, *param)
                tupla_momentum=(list_momentum[0], list_momentum[1], list_momentum[2], list_momentum[3])
                Pixel_Color=Geodesic_Chris(*coords_0, *tupla_momentum , *param)

                print("Progreso:", 4*int(k*Porc_Avance), "%")
                k+=1

                Data_Quadrant=[i, j, Pixel_Color, x, y]
                One_line_data_quadrant.append(Data_Quadrant)
                if (j+1==N_pix_little):
                    All_data_Quadrant.append(One_line_data_quadrant)
                
                
                # El tercer elemento es el color que tiene el pixel, si pone "White" es que es el eje x o z   
    return All_data_Quadrant



def main():
    # Comienzo del tiempo para saber cuanto tarda
    start_time=time.time()
    # Leer el fichero de inputs
    csv_Input= open('./Input/Input.csv', 'r')
    Reader_Input = csv.reader(csv_Input)

    list_Input=[]
    for row in Reader_Input:
        content_input = row[1]
        list_Input.append(content_input)


    csv_Input.close()


    # Masa del agujero negro
    M=eval(list_Input[0])

    # Posicion del Observador y Condiciones Iniciales
#    t_0=eval(list_Input[1])
    r_0=eval(list_Input[2])
#    phi_0=eval(list_Input[3])
#    theta_0= eval(list_Input[4])
#    coords_0=(t_0, r_0, phi_0, theta_0)

    # Numero de Pixeles en un lado, el numero de pixeles total será, N_pix * N_pix
    N_pix=eval(list_Input[5])
    if (N_pix%2)==1: # Para que N_pix sea par y se pueda divir facil en 4 cuadrantes
        N_pix+=1


    # Parametros del Agujero Negro (Spin, Carga electrica y Magnetica, etc)

#    a=eval(list_Input[6])
#    param=(M,a)


    # Definimos un fichero en el que escribir los resultados que nos interesen
    file_Total=open("./Data/Geodesics_Total.csv", "w", newline="")
    csv_Total=csv.writer(file_Total)



    # Pixeles para cada proceso y tamaño de pantalla
    N_pix_little=int(N_pix/2)      # Esto hay que cambiarlo depende del numero de trabajadores o de zonas que te quieras centrar
    L_screen=Screen(r_0, M) # Tamaño de la pantalla




    executor = ProcessPoolExecutor(max_workers=4)

    a=executor.submit(Black_Hole_Geodesic, -L_screen/2, 0, -L_screen/2, 0, N_pix_little, list_Input)
    b=executor.submit(Black_Hole_Geodesic, 0, L_screen/2, -L_screen/2, 0, N_pix_little, list_Input)
    c=executor.submit(Black_Hole_Geodesic, -L_screen/2, 0, 0, L_screen/2, N_pix_little, list_Input)
    d=executor.submit(Black_Hole_Geodesic, 0, L_screen/2, 0, L_screen/2, N_pix_little, list_Input)



    for j in range(N_pix_little): 
        for i in range(N_pix_little):
            csv_Total.writerow(a.result()[j][i])
        for i in range(N_pix_little):
            csv_Total.writerow(b.result()[j][i])

    for j in range(N_pix_little): 
        for i in range(N_pix_little):
            csv_Total.writerow(c.result()[j][i])
        for i in range(N_pix_little):
            csv_Total.writerow(d.result()[j][i])

    print(time.time()-start_time)
    file_Total.close()
    # rnd=random.random()    Usar esto para cuando haga un montecarlo


if __name__ == '__main__':
    main()





