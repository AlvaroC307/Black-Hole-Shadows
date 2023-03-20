# Importar Librerias utiles
import math
import time
import csv
from playsound import playsound
import os


from math import *

from concurrent.futures import *

from Angle_to_Momentum import *
from Solving_Kerr_with_Christoffel import *


def Screen(Factor_Screen, r_0, M):  # Calculo del tamaño de la pantalla
    rho2_Schwarzschild = r_0/2*M

    # Angulo de la sombra para un agujero negro de Schwarzschild con la misma masa
    angle_Schwarzschild = math.asin(
        math.sqrt((27*(rho2_Schwarzschild-1))/(4*(rho2_Schwarzschild**3))))
    
    # Radio para el angulo de schwarzschild
    L_Schwarzschild = r_0*math.tan(angle_Schwarzschild)

    # Multiplicamos por un numero que da el usuario para que haya pantalla para ver la sombra y el espacio correctamente
    L_screen = Factor_Screen * L_Schwarzschild
    return L_screen


# Funcion para dar a cada worker una cantidad de pantalla y que calcule los colores de cada pixel en su apartado
def Black_Hole_Geodesic(x0, x1, y0, y1, N_pix_x, N_pix_y, list_Input, worker):
    #worker es el nombre del trabajador

    # Masa del agujero negro
    M = eval(list_Input[0])

    # Posicion del Observador y Condiciones Iniciales
    t_0 = eval(list_Input[1])
    r_0 = eval(list_Input[2])
    phi_0 = eval(list_Input[3])
    theta_0 = eval(list_Input[4])
    coords_0 = (t_0, r_0, phi_0, theta_0)

    # Parametros del Agujero Negro (Spin, Carga electrica y Magnetica, etc)

    a = eval(list_Input[7])
    param = (M, a)

    # Porcentaje para la Barra de Progreso
    Porc_Avance = 100/(N_pix_x*N_pix_y)

    All_data_Quadrant = [] # Lista donde estarán todos los colores de cada pixel
    Lx = x1-x0 # Tamaño de la pantalla en el eje horizontal
    Ly = y1-y0 # Tamaño de la pantalla en el eje vertical
    paso_x = Lx/N_pix_x # Paso entre cada centro de cada pixel en el eje horizontal
    paso_y = Ly/N_pix_y # Paso entre cada centro de cada pixel en el eje vertical
    # Aunque no lo parezca a primera vista paso_x=paso_y porque L_y es más grande pero también tiene más pixeles. Es importante el equilibrio


    # Esto es para que luego se pongan en el centro del pixel y no en una esquina
    x0 = x0+paso_x/2 
    y0 = y0+paso_y/2

    k = 0
    for i in range(N_pix_y):
        One_line_data_quadrant = []

        for j in range(N_pix_x):
            x = x0+j*paso_x # Avance del eje x
            y = y0+i*paso_y # Avance del eje y
            list_momentum = Screen_to_Momentum(x, y, *coords_0, *param) # Calculo de los momentos para dicho punto
            tupla_momentum = (list_momentum[0], list_momentum[1], list_momentum[2], list_momentum[3])
            Pixel_Color = Geodesic_Chris(*coords_0, *tupla_momentum, *param) # Calculo del color en dicho pixel

            print("Progreso del trabajador " + worker + ":", int(k*Porc_Avance), "%") # Barra de progreso
            k += 1

            Data_Quadrant = [i, j, Pixel_Color, x, y]
            One_line_data_quadrant.append(Data_Quadrant)
            if (j+1 == N_pix_x):
                All_data_Quadrant.append(One_line_data_quadrant) # Escritura de los colores en una lista de listas

            # El tercer elemento es el color que tiene el pixel, si pone "White" es que es el eje x o z
    return All_data_Quadrant


def main():
    # Comienzo del tiempo para saber cuanto tarda el programa en total
    start_time = time.time()

    # Leer el fichero de inputs
    csv_Input = open('./Input/Input.csv', 'r')
    Reader_Input = csv.reader(csv_Input)

    list_Input = [] # Escribir el fichero de inputs en una lista
    for row in Reader_Input:
        content_input = row[1]
        list_Input.append(content_input)

    csv_Input.close()

    # Masa del agujero negro
    M = eval(list_Input[0])

    # Posicion radial del Observador 
    r_0 = eval(list_Input[2])

    # Numero de Pixeles en un lado, el numero de pixeles total será, N_pix * N_pix
    N_pix = eval(list_Input[5])
    if (N_pix % 4) !=0:
        N_pix = N_pix + 4 - (N_pix % 4) # Para que sea facil de dividir por 4 el numero de pixeles

    Factor_Screen=eval(list_Input[6]) # Factor multiplicativo para el tamaño de la pantalla


    # Definimos un fichero en el que escribir los resultados que nos interesen
    file_Total = open("./Data/Geodesics_Total.csv", "w", newline="")
    csv_Total = csv.writer(file_Total)


    # Numero de pixeles en el eje x y en el eje y
    N_pix_x = int(N_pix/4)
    N_pix_y = int(N_pix/2)
    L_screen = Screen(Factor_Screen, r_0, M)  # Tamaño de la pantalla total

    executor = ProcessPoolExecutor(max_workers=8) # Numero de trabajadores que se utilizan

    #Asignar a cada trabajador su parte de la pantalla total, no todos tardan lo mismo
    work_a = executor.submit(Black_Hole_Geodesic, -L_screen/2,
                        -L_screen/4, L_screen/2, 0, N_pix_x, N_pix_y, list_Input, "a")
    work_b = executor.submit(Black_Hole_Geodesic, -L_screen/4, 0,
                        L_screen/2, 0, N_pix_x, N_pix_y, list_Input, "b")
    work_c = executor.submit(Black_Hole_Geodesic, 0, L_screen/4,
                        L_screen/2, 0, N_pix_x, N_pix_y, list_Input, "c")
    work_d = executor.submit(Black_Hole_Geodesic, L_screen/4, L_screen/2,
                        L_screen/2, 0, N_pix_x, N_pix_y, list_Input, "d")
    work_e = executor.submit(Black_Hole_Geodesic, -L_screen/2,
                        -L_screen/4, 0, -L_screen/2, N_pix_x, N_pix_y, list_Input, "e")
    work_f = executor.submit(Black_Hole_Geodesic, -L_screen/4, 0,
                        0, -L_screen/2, N_pix_x, N_pix_y, list_Input, "f")
    work_g = executor.submit(Black_Hole_Geodesic, 0, L_screen/4,
                        0, -L_screen/2, N_pix_x, N_pix_y, list_Input, "g")
    work_h = executor.submit(Black_Hole_Geodesic, L_screen/4, L_screen/2,
                        0, -L_screen/2, N_pix_x, N_pix_y, list_Input, "h") 


    # Escritura de todos los resultados de tal manera que toda una linea horizontal este junta y cada N_pix se cambia de vertical
    for j in range(N_pix_y):
        for i in range(N_pix_x):
            csv_Total.writerow(work_a.result()[j][i])
        for i in range(N_pix_x):
            csv_Total.writerow(work_b.result()[j][i])
        for i in range(N_pix_x):
            csv_Total.writerow(work_c.result()[j][i])
        for i in range(N_pix_x):
            csv_Total.writerow(work_d.result()[j][i])

    for j in range(N_pix_y):
        for i in range(N_pix_x):
            csv_Total.writerow(work_e.result()[j][i])
        for i in range(N_pix_x):
            csv_Total.writerow(work_f.result()[j][i])
        for i in range(N_pix_x):
            csv_Total.writerow(work_g.result()[j][i])
        for i in range(N_pix_x):
            csv_Total.writerow(work_h.result()[j][i])


    current_dir = os.getcwd()
    file_path = current_dir + '/Sounds/Barra_Metal_Cayendo.mp3'

    print((time.time()-start_time)/60, "minutos") #Calculo del tiempo total del programa en minutos
    playsound(file_path)
    file_Total.close() # Cerrar el fichero


if __name__ == '__main__': #Llamar al main()
    main()


