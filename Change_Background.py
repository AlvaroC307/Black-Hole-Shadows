import Background as Bg
import csv
import sys
import math
from Representation import matplot
from Initial_Values import N_pix, Back_Im, theta_0, constantes

def Read_ijxy(file_path:str)->list:
    # Leer la x y la y del fichero de colores
    # Abrir el fichero con los colores a lee
    file_Total_Color = open(file_path + '/Geodesics_Color.csv', 'r')
    Reader_Total_Color = csv.reader(file_Total_Color)

    ijxy_Total=[] # Lista de Listas donde estarán todos los colores como string
    k=0
    for row in Reader_Total_Color:
        ijxy=[row[0], row[1], row[3], row[4]] # El color está en la tercera columna, el resto indican en que lugar está
        ijxy_Total.append(ijxy)

    file_Total_Color.close()
    return ijxy_Total


def Rewrite_Geodesics_Color(file_path:str, ijxy_Total:list)->None:

    file_Position = open(file_path + "/Geodesics_Position_Total.csv", 'r')
    csv_Position = csv.reader(file_Position)
    file_Color = open("./Data/Geodesics_Color.csv", "w", newline="")
    csv_Color = csv.writer(file_Color)


    progreso=100/(N_pix**2)
    k=0
    for row in csv_Position:
        if (row[0]=="Inside"):
            Pixel_Color="Black"
        elif (row[0]=="Orbit"):
            Pixel_Color="Pink"
        else:
            if  Back_Im == "Image":
                Pixel_Color=Bg.Background_Image(float(row[0]), float(row[1]), float(row[2]))
            elif Back_Im == "Colours":
                Pixel_Color=Bg.Sphere_Quadrants(float(row[0]), float(row[1]), float(row[2]))
            else:
                sys.exit("Hay un error, Back_im debe ser Colours o Image, para colores o imagen respectivamente")


        csv_Color.writerow([ijxy_Total[k][0], ijxy_Total[k][1], Pixel_Color, ijxy_Total[k][2], ijxy_Total[k][3]])
        k+=1
        print(f"Lleva un {k*progreso} %")



def main()->None:

    a_value=constantes["a"] # Esto tengo que hacerlo porque f"constantes["a"]" da error por las multiples comillas
    Q_e_value=constantes["Q_e"]

    # Encontramos el nombre de la carpeta donde se guardan los datos a leer
    if theta_0 == math.pi/2:
        file_path =f"./Data/Data_Base_Position_Total/a={a_value},Q_e={Q_e_value}/theta_0=equator/{N_pix}x{N_pix}"
    elif theta_0 == 0:
        file_path =f"./Data/Data_Base_Position_Total/a={a_value},Q_e={Q_e_value}/theta_0=0/{N_pix}x{N_pix}"
    else:
        sys.exit("Ese valor de theta_0 no está cargado en la base de datos. Simulalo independiente usando Shadow_Multiprocess.py")

    ijxy_Total=Read_ijxy(file_path) # Obtenemos los datos de los valores de la x e y de cada punto
    Rewrite_Geodesics_Color(file_path, ijxy_Total) # Reescribimos el color en Geodesics_Color 
    matplot() # Se genera la imagen

if __name__ == '__main__':
    main()