# Leer los ficheros de resultados para representarlo en un dibujo
import csv
import matplotlib.pyplot as plt # Esto es para el plot
import matplotlib.colors as mcolors # Esto es para cambiar los colores a valores numéricos
import numpy as np # Esto es para los array al cambiar de los colores a valores numericos


def matplot(N_pix):
    # Abrir el fichero con los colores a lee
    file_Total = open('./Data/Geodesics_Total.csv', 'r')
    Reader_Total = csv.reader(file_Total)

    Color_Line=[] # Lista donde se apuntan los colores de una linea en el eje x entera antes de pasarla a Color_Total
    Color_Total=[] # Lista de Listas donde estarán todos los colores como string
    k=0
    for row in Reader_Total:
        content=row[2] # El color está en la tercera columna, el resto indican en que lugar está
        Color_Line.append(content)
        k+=1
        if k==N_pix:
            Color_Total.append(Color_Line)
            k=0
            Color_Line=[]

    # Cambio de la lista de listas de colores en string a un array de colores como lista de numeros en RGBA para matplotlib
    color_array = np.array([[mcolors.to_rgba(color) for color in row] for row in Color_Total])

    # Create a figure and plot the image
    fig, ax = plt.subplots(figsize=(5, 5)) # figsize habla sobre el tamaño de la imagen
    ax.imshow(color_array)

    # Quitar los ejes, guardar y mostrar en pantalla la imagen 
    ax.axis('off')
    plt.savefig('./Graphics/Black_Hole_Image.pdf', bbox_inches='tight') # Guardar la imagen como un pdf
    plt.savefig('./Graphics/Black_Hole_Image.png', bbox_inches='tight') # Guardar la imagen como un png
    plt.show() # Mostrar la imagen

   




def main():
    csv_Input = open('./Input/Input.csv', 'r')
    Reader_Input = csv.reader(csv_Input)

    list_Input = []
    for row in Reader_Input:
        content_input = row[1]
        list_Input.append(content_input)

    csv_Input.close()

    # Numero de Pixeles en un lado, el numero de pixeles total será, N_pix * N_pix
    N_pix = eval(list_Input[5])
    if (N_pix % 4) !=0:
        N_pix = N_pix + 4 - (N_pix % 4) # Para que sea facil de dividir por 4 el numero de pixeles

    matplot(N_pix)

if __name__ == '__main__':
    main()
