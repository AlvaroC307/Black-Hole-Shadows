# Leer los ficheros de resultados para representarlo en un dibujo
import csv
import matplotlib.pyplot as plt # Esto es para el plot
import matplotlib.colors as mcolors # Esto es para cambiar los colores a valores numéricos
import numpy as np # Esto es para los array al cambiar de los colores a valores numericos
from Initial_Values import N_pix

def matplot()->None:

    #Abrir el fichero Input para saber si el usuario quiere con colores o con una imagen dada
    # Leer el fichero de inputs
    csv_Input = open('./Input/Input.csv', 'r')
    Reader_Input = csv.reader(csv_Input)

    list_Input = [] # Escribir el fichero de inputs en una lista
    for row in Reader_Input:
        content_input = row[1]
        list_Input.append(content_input)

    csv_Input.close()

    # "C" es para la funcion de los cuadrantes de la esfera de colores. "I" es si ha dado el usuario una imagen de fondo.
    Back_Im=list_Input[7]



    # Abrir el fichero con los colores a lee
    file_Total = open('./Data/Geodesics_Color.csv', 'r')
    Reader_Total = csv.reader(file_Total)

    Color_Line=[] # Lista donde se apuntan los colores de una linea en el eje x entera antes de pasarla a Color_Total
    Color_Total=[] # Lista de Listas donde estarán todos los colores como string
    k=0
    for row in Reader_Total:
        content=row[2] # El color está en la tercera columna, el resto indican en que lugar está

        if Back_Im=="I":
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

    if Back_Im=="I":
        color_array = Color_Total
    elif Back_Im=="C":
        color_array = np.array([[mcolors.to_rgb(color) for color in row] for row in Color_Total])
    

    # Create a figure and plot the image
    fig, ax = plt.subplots(figsize=(5, 5)) # figsize habla sobre el tamaño de la imagen
    ax.imshow(color_array)

    # Quitar los ejes, guardar y mostrar en pantalla la imagen 
    ax.axis('off')
    plt.savefig('./Graphics/Black_Hole_Image.pdf', bbox_inches='tight') # Guardar la imagen como un pdf
    plt.savefig('./Graphics/Black_Hole_Image.png', bbox_inches='tight') # Guardar la imagen como un png
    plt.show() # Mostrar la imagen



def main()->None:
    matplot()

if __name__ == '__main__':
    main()
