# Leer los ficheros de resultados para representarlo en un dibujo
import csv
import math
import matplotlib.pyplot as plt # Esto es para el plot
import matplotlib.colors as mcolors # Esto es para cambiar los colores a valores numéricos
import numpy as np # Esto es para los array al cambiar de los colores a valores numericos
from Initial_Values import N_pix, Back_Im, Factor_Screen, M, axis

def matplot()->None:

    # Abrir el fichero con los colores a lee
    file_Total = open('./Data/Geodesics_Color.csv', 'r')
    Reader_Total = csv.reader(file_Total)

    Color_Line=[] # Lista donde se apuntan los colores de una linea en el eje x entera antes de pasarla a Color_Total
    Color_Total=[] # Lista de Listas donde estarán todos los colores como string
    k=0
    for row in Reader_Total:
        content=row[2] # El color está en la tercera columna, el resto indican en que lugar está

        if Back_Im=="Image":
            if content=="Black":
                content=[0,0,0]
            elif content=="Pink":
                content=[255,105,180]
            else:
                content=eval(content) 
            
        Color_Line.append(content)
        k+=1
        if k==N_pix:
            Color_Total.append(Color_Line)
            k=0
            Color_Line=[]


    # Cambio de la lista de listas de colores en string a un array de colores como lista de numeros en RGBA para matplotlib
    # "C" es para la funcion de los cuadrantes de la esfera de colores. "I" es si ha dado el usuario una imagen de fondo.

    if Back_Im=="Image":
        color_array = Color_Total
    elif Back_Im=="Colours":
        color_array = np.array([[mcolors.to_rgb(color) for color in row] for row in Color_Total])

    # Create a figure and plot the image
    fig, ax = plt.subplots(figsize=(5, 5)) # figsize habla sobre el tamaño de la imagen

    if axis=="Yes":

        # Radio de la sombra del agujero negro de Schwarzschild equivalente
        L_Schwarzschild = 3*math.sqrt(3)*M
        # Multiplicamos por un numero que da el usuario para que haya pantalla para ver la sombra y el espacio correctamente
        L_screen = Factor_Screen * L_Schwarzschild

        ax.imshow(color_array, extent=[-L_screen/2, L_screen/2, -L_screen/2, L_screen/2])

        # Ajustar los límites de los ejes para que vayan de -l_screen/2 a L/screen/2
        ax.set_xlim(-L_screen/2, L_screen/2)
        ax.set_ylim(-L_screen/2, L_screen/2)

        # Establecer la relación de aspecto de la imagen para evitar distorsión
        ax.set_aspect('auto')

        # Reparametrizar las marcas de los ejes (ticks)
        num_ticks = 9  # Número de ticks que deseas 

        # Ticks para el eje x y eje y, distribuidos de manera uniforme
        ticks=np.linspace(-L_screen/2, L_screen/2, num_ticks)
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
              
        # Etiquetas de los ticks 
        tick_labels = [f"{tick:.2f}" for tick in ticks] #.2f en el formato de cadena indica que se deben mostrar dos cifras después del punto decimal.
        ax.set_xticklabels(tick_labels)
        ax.set_yticklabels(tick_labels)
        ax.axis("on")
    else:
        ax.imshow(color_array)
        ax.axis('off')

    # Guardar y mostrar en pantalla la imagen 
    
    plt.savefig('./Graphics/Black_Hole_Image.pdf', bbox_inches='tight') # Guardar la imagen como un pdf
    plt.savefig('./Graphics/Black_Hole_Image.png', bbox_inches='tight') # Guardar la imagen como un png
    plt.show() # Mostrar la imagen


def locate_error_in_data()->list:

    file_Position = open("./Data/Geodesics_Position_Total.csv", 'r')
    csv_Position = csv.reader(file_Position)

    position_r=[]
    for row in csv_Position:
        if row[0]=="Inside" or row[0] == "Orbit":
            position_r.append(row[0])
        else:
            position_r.append(float(row[0]))

    Problem_Source = []

    for i in range(len(position_r) - 2):  # Recorremos hasta el antepenúltimo elemento
        if position_r[i] == "Inside" and isinstance(position_r[i+1], (int, float)) and position_r[i+2] == "Inside":
            print(f"Hay una combinacion Inside-Outside-Inside en: {i}, {i+1}, {i+2}")
            Problem_Source.append(i+1)
    
    return Problem_Source


def main()->None:

    Problem_Source = locate_error_in_data()

    if Problem_Source !=[]:
        print(f"Las fuentes de problemas pueden ser los pixeles: {Problem_Source}")    

    matplot()

if __name__ == '__main__':

    main()
