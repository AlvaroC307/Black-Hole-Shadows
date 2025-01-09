# Importar Librerias utiles
import math
import time
import csv
from playsound import playsound
import os
import concurrent.futures as cf
from Angle_to_Momentum import Screen_to_Momentum
from Solving_Geodesic_Backwards_RayT import Geodesic_Chris
from Initial_Values import M, r_0, Factor_Screen, N_pix, sound
from Representation import matplot

def Finish_sound()->None:
    sound_path = "./Sounds/" + sound.strip()
    
    if os.path.exists(sound_path):
        playsound(sound_path)
    else:
        print(f"El archivo de sonido {sound_path} no existe.")




def Screen()->float:  # Calculo del tamaño de la pantalla
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
def Black_Hole_Geodesic(x0:float, x1:float, y0:float, y1:float, N_pix_x:int, N_pix_y:int, worker:str)->list:
    #worker es el nombre del trabajador

    # Porcentaje para la Barra de Progreso
    Porc_Avance = 100/(N_pix_x*N_pix_y)

    All_color_Quadrant = [] # Lista donde estarán todos los colores de cada pixel
    All_position_Quadrant = [] # Lista donde estarán todos los colores de cada pixel
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
        One_line_color_quadrant = []
        One_line_position_quadrant = []

        for j in range(N_pix_x):
            x = x0+j*paso_x # Avance del eje x
            y = y0+i*paso_y # Avance del eje y
            tuple_momentum = Screen_to_Momentum(x, y) # Calculo de los momentos para dicho punto

            try:
                Pixel_Data= Geodesic_Chris(*tuple_momentum)
                Pixel_Color = Pixel_Data[0] # Calculo del color en dicho pixel
                Pixel_Position= Pixel_Data[1]

            except Exception as e:
                # code to handle the error
                print("An error occurred", e)
                print("In the points:", x, y)

            print("Progreso del trabajador " + worker + ":", int(k*Porc_Avance), "%") # Barra de progreso
            k += 1

            Color_Quadrant = [i, j, Pixel_Color, x, y]
            One_line_color_quadrant.append(Color_Quadrant)
            One_line_position_quadrant.append(Pixel_Position)
            if (j+1 == N_pix_x):
                All_color_Quadrant.append(One_line_color_quadrant) # Escritura de los colores en una lista de listas
                All_position_Quadrant.append(One_line_position_quadrant) # Escritura de las posiciones en una lista de listas

            # El tercer elemento es el color que tiene el pixel, si pone "White" es que es el eje x o z
    return [All_color_Quadrant, All_position_Quadrant]


def main()->None:
    # Comienzo del tiempo para saber cuanto tarda el programa en total
    start_time = time.time()

    # Definimos un fichero en el que escribir los resultados que nos interesen
    file_Color = open("./Data/Geodesics_Color.csv", "w", newline="")
    csv_Color = csv.writer(file_Color)
    file_Position = open("./Data/Geodesics_Position_Total.csv", "w", newline="")
    csv_Position = csv.writer(file_Position)


    # Numero de pixeles en el eje x y en el eje y
    N_pix_x = int(N_pix/4)
    N_pix_y = int(N_pix/2)
    L_screen = Screen()  # Tamaño de la pantalla total

    executor = cf.ProcessPoolExecutor(max_workers=8) # Numero de trabajadores que se utilizan

    #Asignar a cada trabajador su parte de la pantalla total, no todos tardan lo mismo
    
    work_a = executor.submit(Black_Hole_Geodesic, -L_screen/2,
                        -L_screen/4, L_screen/2, 0, N_pix_x, N_pix_y, "a")
    work_b = executor.submit(Black_Hole_Geodesic, -L_screen/4, 0,
                        L_screen/2, 0, N_pix_x, N_pix_y, "b")
    work_c = executor.submit(Black_Hole_Geodesic, 0, L_screen/4,
                        L_screen/2, 0, N_pix_x, N_pix_y, "c")
    work_d = executor.submit(Black_Hole_Geodesic, L_screen/4, L_screen/2,
                        L_screen/2, 0, N_pix_x, N_pix_y, "d")
    work_e = executor.submit(Black_Hole_Geodesic, -L_screen/2,
                        -L_screen/4, 0, -L_screen/2, N_pix_x, N_pix_y, "e")
    work_f = executor.submit(Black_Hole_Geodesic, -L_screen/4, 0,
                        0, -L_screen/2, N_pix_x, N_pix_y, "f")
    work_g = executor.submit(Black_Hole_Geodesic, 0, L_screen/4,
                        0, -L_screen/2, N_pix_x, N_pix_y, "g")
    work_h = executor.submit(Black_Hole_Geodesic, L_screen/4, L_screen/2,
                        0, -L_screen/2, N_pix_x, N_pix_y, "h") 


    # Escritura de todos los resultados de tal manera que toda una linea horizontal este junta y cada N_pix se cambia de vertical
    for j in range(N_pix_y):
        for i in range(N_pix_x):
            csv_Color.writerow(work_a.result()[0][j][i])
            csv_Position.writerow(work_a.result()[1][j][i])
        for i in range(N_pix_x):
            csv_Color.writerow(work_b.result()[0][j][i])
            csv_Position.writerow(work_b.result()[1][j][i])
        for i in range(N_pix_x):
            csv_Color.writerow(work_c.result()[0][j][i])
            csv_Position.writerow(work_c.result()[1][j][i])
        for i in range(N_pix_x):
            csv_Color.writerow(work_d.result()[0][j][i])
            csv_Position.writerow(work_d.result()[1][j][i])

    for j in range(N_pix_y):
        for i in range(N_pix_x):
            csv_Color.writerow(work_e.result()[0][j][i])
            csv_Position.writerow(work_e.result()[1][j][i])
        for i in range(N_pix_x):
            csv_Color.writerow(work_f.result()[0][j][i])
            csv_Position.writerow(work_f.result()[1][j][i])
        for i in range(N_pix_x):
            csv_Color.writerow(work_g.result()[0][j][i])
            csv_Position.writerow(work_g.result()[1][j][i])
        for i in range(N_pix_x):
            csv_Color.writerow(work_h.result()[0][j][i])
            csv_Position.writerow(work_h.result()[1][j][i])


    file_Color.close() # Cerrar el fichero
    file_Position.close()


    Finish_sound()

    print(f"The program has run for {(time.time()-start_time)/60}, minutos") #Calculo del tiempo total del programa en minutos
    
    matplot() # Cuando compile el programa se ejecuta representation automaticamente



if __name__ == '__main__': #Llamar al main()
    main()


